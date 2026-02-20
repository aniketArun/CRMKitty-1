import pytest
import requests
from conftest import base_url

customer_id:int = None

@pytest.fixture
def _customer_id()->int:
    return customer_id


def test_create_customer(auth_headers):
    url:str = f"{base_url}/customer"

    data = {
        "first_name":"john"
    }

    response =  requests.post(url=url, json=data, headers=auth_headers)

    assert response.status_code == 201
    global customer_id
    print(response.json())
    customer_id = response.json()['id']


def test_get_all_customers(auth_headers):
    url:str = f"{base_url}/customer"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200

def test_get_customer_by_id(_customer_id, auth_headers):
    url:str = f"{base_url}/customer/{_customer_id}"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200
    assert response.json()['id'] == _customer_id

def test_put_customer_by_id(_customer_id, auth_headers):
    url:str = f"{base_url}/customer/{_customer_id}"
    data = {
        "last_name":"patil"
    }
    response = requests.put(url=url, json=data, headers=auth_headers)

    assert response.status_code == 202
    assert response.json()['last_name'] == data['last_name']

def test_delete_customer_by_id(_customer_id, auth_headers):
    url:str = f"{base_url}/customer/{_customer_id}"

    response = requests.delete(url=url, headers=auth_headers)

    assert response.status_code == 202
