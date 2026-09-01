import pytest
import json



def test_get_product(products_client):
    response = products_client.get_product(1)
    assert response.status_code == 200
    data = response.json()
    print(json.dumps(data, indent=2))
    assert data["id"] == 1
    assert "title" in data
    assert "price" in data

def test_get_non_existing_product(products_client):
    response = products_client.get_product(999)
    assert response.status_code == 404

