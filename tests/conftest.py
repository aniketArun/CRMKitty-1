import pytest
import requests
import os

from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASEURL")



@pytest.fixture(scope="session")
def bearer_token():
    url = f"{base_url}/auth/token"
    username = os.getenv("SYSTEM_USER")
    password = os.getenv("SYSTEM_PWD")
    # Example: fetch token from auth endpoint

    # Send as form data, not JSON 
    response = requests.post( 
                            url, 
                            data={ "username": username, "password": password }, 
                            headers={"Content-Type": "application/x-www-form-urlencoded"} 
                             ) 
    response.raise_for_status() 
    return response.json()["access_token"]

@pytest.fixture
def auth_headers(bearer_token):
    return {"Authorization": f"Bearer {bearer_token}"}
