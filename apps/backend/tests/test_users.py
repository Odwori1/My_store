import uuid
from tests.conftest import client

def unique_email(base="user"):
    return f"{base}_{uuid.uuid4().hex}@example.com"

def test_create_user(client):
    email = unique_email()
    response = client.post("/users/", json={
        "name": "Test User",
        "email": email,
        "password": "secret123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == email
    assert "id" in data

def test_read_users(client):
    email = unique_email()
    client.post("/users/", json={"name": "Read Me", "email": email, "password": "pass123"})
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_user(client):
    email = unique_email()
    res = client.post("/users/", json={"name": "Update Me", "email": email, "password": "pass123"})
    user_id = res.json()["id"]
    response = client.put(f"/users/{user_id}", json={"name": "Updated Name", "is_active": False})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"
    assert data["is_active"] is False

def test_delete_user(client):
    email = unique_email()
    res = client.post("/users/", json={"name": "Delete Me", "email": email, "password": "pass123"})
    user_id = res.json()["id"]
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "User deleted"

