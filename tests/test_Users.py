from fastapi.testclient import TestClient
import sys, os
import pytest

# pastikan folder project ada di path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

# Fixture untuk membuat user sebelum test lainnya
@pytest.fixture
def created_user():
    payload = {
        "username": "user123",
        "email": "user123@example.com",
        "password": "Password1!",
        "role": "staff"
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    return response.json()  # mengembalikan dict user termasuk "id"

def test_create_user():
    payload = {
        "username": "user456",
        "email": "user456@example.com",
        "password": "Password2!",
        "role": "staff"
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["username"] == "user456"
    assert data["email"] == "user456@example.com"
    assert data["role"] == "staff"

def test_read_user(created_user):
    user_id = created_user["id"]
    response = client.get(f"/users/{user_id}?role=admin")  # ❗ role=admin penting
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["username"] == "user123"

def test_update_user(created_user):
    user_id = created_user["id"]
    payload = {
        "username": "user123updated",
        "email": "user123updated@example.com",
        "role": "staff"   
    }
    response = client.put(f"/users/{user_id}?role=admin", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "user123updated"
    assert data["email"] == "user123updated@example.com"
    assert data["role"] == "staff"


def test_delete_user(created_user):
    user_id = created_user["id"]
    response = client.delete(f"/users/{user_id}?role=admin")  # ❗ role=admin
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

    # pastikan user sudah terhapus
    response = client.get(f"/users/{user_id}?role=admin")
    assert response.status_code == 404
