from fastapi import status

from routers.users import get_current_user, get_db
from utils import app, client, override_get_current_user, \
                  override_get_db, test_user, TestingSessionLocal, Todos


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


# ===== GET =====

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'Test'
    assert response.json()['first_name'] == 'Test'
    assert response.json()['last_name'] == 'Example'
    assert response.json()['email'] == 'test@example.com'
    assert response.json()['role'] == 'admin'

# ===== PUT =====

def test_change_password_sucess(test_user):
    response = client.put("/user/password", json={
        "password": "999abc", "new_password": "666xyz"
    })
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/password", json={
        "password": "xxxxxx", "new_password": "666xyz"
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}
