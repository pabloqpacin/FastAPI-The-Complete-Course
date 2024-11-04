from fastapi import status

from models import Todos
from utils import client, test_todo, TestingSessionLocal

# ===== GET =====

def test_read_all_authenticated(test_todo):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        'id': 1, 'title': 'Learn to code!', 'description': 'supdawg',
        'priority': 4, 'complete': False, 'owner_id': 1
    }]

def test_read_one_authenticated(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'id': 1, 'title': 'Learn to code!', 'description': 'supdawg',
        'priority': 4, 'complete': False, 'owner_id': 1
    }

def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}

# ===== POST =====

def test_create_todo():
    request_data = {
        'title': 'New Todo!',
        'description': 'supdawg',
        'priority': 3,
        'complete': False
    }
    response = client.post('/todo', json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    # Check the database directly for the created record
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.title == 'New Todo!').first()
    db.close()
    assert model.title == request_data['title']
    assert model.description == request_data['description']
    assert model.priority == request_data['priority']
    assert model.complete == request_data['complete']

# ===== PUT =====

def test_update_todo(test_todo):
    request_data = {
        'title': 'Update Todo!',
        'description': 'supdawg',
        'priority': 3,
        'complete': False        
    }
    response = client.put('/todo/1', json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    db.close()
    assert model.title == 'Update Todo!'

def test_update_todo_not_found():
    request_data = {
        'title': 'Update Todo!',
        'description': 'supdawg',
        'priority': 3,
        'complete': False        
    }
    response = client.put('/todo/999', json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}

# ===== DELETE =====

def test_delete_todo(test_todo):
    response = client.delete('/todo/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    db.close()
    assert model is None

def test_delete_todo_not_found():
    response = client.delete('/todo/999')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}
