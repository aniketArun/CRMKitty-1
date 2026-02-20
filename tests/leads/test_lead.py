import pytest
import requests
from conftest import base_url

lead_id:int = None

@pytest.fixture
def _lead_id():
    return lead_id

def test_get_all_leads(auth_headers):
    url:str = f"{base_url}/leads"

    response = requests.get(url=url, headers=auth_headers)
    
    if response.status_code == 404:
        assert response.json()['detail'] == "Lead not Fount!"
    
    else:
        assert response.status_code == 200

def test_create_lead(auth_headers):
    url:str = f"{base_url}/leads"

    data = {
        "first_name":"Raj",
        "last_name":"Govardhan"
    }

    response = requests.post(url=url, json=data, headers=auth_headers)

    assert response.status_code == 201
    assert response.json()['first_name'] == data['first_name']
    global lead_id
    lead_id = response.json()['id']

def test_get_lead_by_id(_lead_id, auth_headers):
    url:str = f"{base_url}/leads/{_lead_id}"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 202
    assert response.json()['id'] == _lead_id

def test_update_lead_by_id(_lead_id, auth_headers):
    url:str = f"{base_url}/leads/{_lead_id}"

    data = {
        "email":"test.demo@mail.co"
    }
    response = requests.patch(url=url, json=data, headers=auth_headers)

    assert response.status_code == 202
    assert response.json()['email'] == data['email']

def test_delete_lead_by_id(_lead_id, auth_headers):

    url:str = f"{base_url}/leads/{_lead_id}"

    response = requests.delete(url=url, headers=auth_headers)

    assert response.status_code == 202