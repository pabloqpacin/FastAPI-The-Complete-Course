from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# # env with os & dotenv innit

# SQLALCHEMY_DATABASE_URL='sqlite:///./todosapp.db'
# SQLALCHEMY_DATABASE_URL='postgresql://fastapi:s_clpa59Bs?D]BP<AgI@postgresql:5010/fastapi'
SQLALCHEMY_DATABASE_URL='postgresql://fastapi:s_clpa59Bs?D]BP<AgI@postgresql:5432/fastapi'

# engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


