from datetime import timedelta

from fastapi import status, HTTPException
from jose import jwt
import pytest

from routers.auth import authenticate_user, create_access_token, \
                         get_current_user, get_db, SECRET_KEY, ALGORITHM
from utils import app, client, override_get_current_user, \
                  override_get_db, test_user, TestingSessionLocal, Todos


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


# ===== ... =====

def test_authenticate_user(test_user):
    db = TestingSessionLocal()

    authenticated_user = authenticate_user(test_user.username, '999abc', db)
    assert authenticated_user is not None
    assert authenticated_user.username == test_user.username

    non_existent_user = authenticate_user('Wrong_Username', '999abc', db)
    assert non_existent_user is False

    wrong_password_user = authenticate_user(test_user.username, 'xxxxxx', db)
    assert wrong_password_user is False

def test_create_access_token():
    username = 'Test'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_delta)
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded_token['sub'] == username
    assert decoded_token['id'] == user_id
    assert decoded_token['role'] == role

@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {'sub': 'testuser', 'id': 1, 'role': 'admin'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    user = await get_current_user(token=token)
    assert user ==  {'username': 'testuser', 'id': 1, 'user_role': 'admin'}
    
@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {'role': 'admin'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)

    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate user'
