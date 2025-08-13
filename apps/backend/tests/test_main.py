import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)
client = TestClient(app)

def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.on_event("startup")
def setup():
    Base.metadata.create_all(bind=engine)

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product():
    response = client.post("/products/", json={"name": "Laptop", "price": 1200.5})
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

