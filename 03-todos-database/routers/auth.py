from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from models import Users


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

    # openssl rand -hex 32
SECRET_KEY='a3f34163c39774c189289aacc2629768423f54a0fe55c8058714b3c976ca984a'
ALGORITHM='HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

# Verify the token as a dependency in our API requests
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

class Token(BaseModel):
    access_token:str
    token_type:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

# def authenticate_user(username:str,password:str,db:Session):
def authenticate_user(username:str,password:str,db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

def create_access_token(username:str,user_id:int,role:str,expires_delta:timedelta):
    encode={'sub':username,'id':user_id,'role':role}
    expires=datetime.now(timezone.utc)+expires_delta
    # expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get('sub')
        user_id:int=payload.get('id')
        user_role:str=payload.get('role')
        if username is None or user_id is None:
            raise credentials_exception
        return {"username":username,"id":user_id,'user_role':user_role}
    except JWTError:
        raise credentials_exception

# ---

# ===== POST =====

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,
                      create_user_request:CreateUserRequest):
    # create_user_model = Users(**create_user_request.model_dump()) # won't work bc password, not hashed_password
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        is_active=True
    )
    db.add(create_user_model)
    db.commit()
    # db.refresh(create_user_model)  # Refresh the object to get the generated ID
    # return {"msg": "User created successfully", "user_id": create_user_model.id}

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate":"Bearer"},
        )
    access_token_expires=timedelta(minutes=20)
    access_token=create_access_token(user.username,user.id,user.role,access_token_expires)
    return {"access_token":access_token,"token_type":"bearer"}

