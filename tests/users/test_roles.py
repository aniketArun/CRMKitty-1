import requests
import pytest
from conftest import base_url

role_id:int = None

@pytest.fixture
def _role_id():
    return role_id

def test_create_role(auth_headers):
    url:str = f"{base_url}/role"

    data = {
        "name": "sales_manager",
        "permissions": [
                "create product"
            ],
        "description": "Sales manager role to manage sale module"
    }
    response = requests.post(url=url, json=data, headers=auth_headers)
    global role_id
    role_id = response.json()['id']
    assert response.status_code == 201

def test_get_all_roles(auth_headers):
    url:str = f"{base_url}/role"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200
    

def test_put_role_by_id(_role_id, auth_headers):

    url:str = f"{base_url}/role/{_role_id}"

    data = {
        "name":"product_manager"
    }

    response = requests.put(url=url, json=data, headers=auth_headers)

    assert response.status_code == 200
    assert response.json()['name'] == data['name']