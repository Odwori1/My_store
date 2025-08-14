import uuid
from tests.conftest import client

def unique_product_name(base="Product"):
    return f"{base}_{uuid.uuid4().hex}"

def test_create_product(client):
    name = unique_product_name()
    response = client.post("/products/", json={
        "name": name,
        "category": "Electronics",
        "cost_price": 1000.0,
        "sale_price": 1200.5,
        "quantity": 10,
        "reorder_level": 5
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == name
    assert data["category"] == "Electronics"

def test_read_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_product(client):
    name = unique_product_name()
    res = client.post("/products/", json={
        "name": name,
        "category": "Electronics",
        "cost_price": 300.0,
        "sale_price": 400.0,
        "quantity": 15
    })
    product_id = res.json()["id"]
    response = client.put(f"/products/{product_id}", json={"name": name+"_Updated", "sale_price": 450.0})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == name+"_Updated"
    assert float(data["sale_price"]) == 450.0

def test_delete_product(client):
    name = unique_product_name()
    res = client.post("/products/", json={
        "name": name,
        "category": "Electronics",
        "cost_price": 200.0,
        "sale_price": 300.0,
        "quantity": 5
    })
    product_id = res.json()["id"]
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Product deleted"

