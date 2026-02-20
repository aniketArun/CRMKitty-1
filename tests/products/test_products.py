from conftest import base_url, auth_headers
import pytest
import requests


product_id = None

@pytest.fixture
def _product_id():
    return product_id

def test_create_product(auth_headers):
    url:str = f"{base_url}/product"
    data = {
        "product_name":"VisaFlow",
        "sku_code":"PRD0002"
    }
    response = requests.post(url=url, json=data, headers=auth_headers)

    assert response.status_code == 201
    global product_id
    product_id = response.json()['id']

def test_get_all_products(auth_headers):
    url:str = f"{base_url}/product"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200


def test_get_product_by_id(_product_id, auth_headers):
    url = f"{base_url}/product/{_product_id}"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200

    assert response.json()['id'] == _product_id

def test_update_product_by_id(_product_id, auth_headers):
    url = f"{base_url}/product/{_product_id}"
    data = {
        "description":"This is Financial Service product"
    }

    response = requests.put(url=url, json=data, headers=auth_headers)

    assert response.status_code == 202
    assert response.json()['description'] == data['description']

def test_delete_product_by_id(_product_id, auth_headers):
    url = f"{base_url}/product/{_product_id}"

    response = requests.delete(url=url, headers=auth_headers)

    assert response.status_code == 202

