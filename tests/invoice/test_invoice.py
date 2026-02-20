from conftest import auth_headers, base_url
import pytest
import requests
from datetime import date
invoice_id:int = None

@pytest.fixture
def _invoice_id()->int:
    return invoice_id

@pytest.mark.skip
def test_create_invoice(auth_headers):
    url = f"{base_url}/invoice"

    data = {
        "due_date":date.today()
    }

    response = requests.post(url=url, json=data, headers=auth_headers)

    assert response.status_code == 200

def test_get_all_invoices(auth_headers):
    url = f"{base_url}/invoice"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200