from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv(dotenv_path="../.env.development", override=True)

POSTGRES_USER = os.getenv('POSTGRES_USER',"fastapi")
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', "postgresql")
POSTGRES_PORT = os.getenv('POSTGRES_PORT',5432)
POSTGRES_DB = os.getenv('POSTGRES_DB',"fastapi")

USE_SQLITE = os.getenv('USE_SQLITE', 'false').lower() == 'true'

if USE_SQLITE:
    # SQLite configuration for Testing with GH Actions
    SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
else:
    # Default PostgreSQL configuration
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

