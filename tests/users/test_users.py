import requests
from conftest import base_url
import pytest

user_id = None

def test_get_user(auth_headers):
    url = f"{base_url}/users"
    response = requests.get(url=url, headers=auth_headers)
    assert response.status_code == 200
    
@pytest.fixture
def user_id_():
    global user_id
    return user_id

def test_create_user(auth_headers):
    url = f"{base_url}/users"
    data = {
        "first_name": "Gaurav",
        "last_name": "Chaudhari",
        "email": "gaurav@example.com",
        "mobile": "47384974498",
        "location": "Nashik, MH India",
        "role": 0,
        "avatar": "public/gaurav.jpg",
        "password": "user123"
        }
    response = requests.post(url=url, json=data, headers=auth_headers)

    assert response.status_code == 201

    assert response.json()['email'] == data['email']

    global user_id
    user_id = response.json()['id']

def test_get_user_by_id(user_id_, auth_headers):
    url:str = f"{base_url}/users/{user_id_}"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200
    print(response.json())
    assert response.json()['id'] == user_id_

def test_put_user_by_id(user_id_, auth_headers):
    url:str = f"{base_url}/users/{user_id_}"

    data = {
        "first_name" : "Sanket"
    }

    response = requests.put(url=url, json=data, headers=auth_headers)

    assert response.status_code == 202
    assert response.json()['first_name'] == data['first_name']

def test_delete_user_by_id(user_id_, auth_headers):
    url:str = f"{base_url}/users/{user_id_}"

    response = requests.delete(url=url, headers=auth_headers)

    assert response.status_code == 200