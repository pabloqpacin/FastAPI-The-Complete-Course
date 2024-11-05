from fastapi import status

from routers.admin import get_current_user, get_db
from utils import app, client, override_get_current_user, \
                  override_get_db, test_todo, TestingSessionLocal, Todos


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


# ===== GET =====

def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        'id': 1, 'title': 'Learn to code!', 'description': 'supdawg',
        'priority': 4, 'complete': False, 'owner_id': 1
    }]

# ===== DELETE =====

def test_admin_delete_todo(test_todo):
    response = client.delete("/admin/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    db.close()
    assert model is None

def test_admin_delete_todo_not_found():
    response = client.delete("/admin/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}
