from typing import Generator

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from main import app
from models import Users, Todos
from routers.auth import bcrypt_context


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

# Test fixture for creating and cleaning up a test user
@pytest.fixture
def test_user() -> Todos:
    user = Users(
        username="Test", email="test@example.com", first_name="Test", last_name="Example",
        hashed_password=bcrypt_context.hash("999abc"), role="admin",
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    db.query(Users).delete()  # Cleaner ORM-based deletion
    db.commit()
    db.close()