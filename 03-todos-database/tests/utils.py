from typing import Generator

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from main import app
from models import Todos
from routers.todos import get_db, get_current_user


# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Override FastAPI dependencies
def override_get_db() -> Generator:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user() -> dict:
    return {'username': 'test', 'id': 1, 'user_role': 'admin'}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# Test client
client = TestClient(app)

# Test fixture for creating and cleaning up a test todo db
@pytest.fixture
def test_todo() -> Todos:
    todo = Todos(
        title="Learn to code!", description="supdawg", priority=4, complete=False, owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    db.query(Todos).delete()  # Cleaner ORM-based deletion
    db.commit()
    db.close()
