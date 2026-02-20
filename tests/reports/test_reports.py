from conftest import auth_headers, base_url
import pytest
import requests

report_id:int = None

@pytest.fixture
def _report_id()->int:
    return report_id

def test_create(auth_headers):
    url = f"{base_url}/report"

    data = {
        "company_id": 123,
        "title": "Test Report 1",
        "customer_id": 456,
        "report_summary": "This is a summary of the test report.",
        "test_cases": [
            {
            "testcase1": "Passed"
            },
            {
            "testcase2": "Failed"
            }
        ],
        "remarks": "Initial testing completed.",
        "status": "NEW",
        "created_by": 1,
        "created_at": "2026-02-20T17:50:00",
        "updated_at": None
        }


    response = requests.post(url=url, json=data, headers=auth_headers)

    assert response.status_code == 201
    global report_id
    report_id = response.json()['id']

def test_get_report_by_id(_report_id, auth_headers):
    url = f"{base_url}/report/{_report_id}"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200
    assert response.json()['id'] == _report_id

def test_get_all_reports(auth_headers):
    url = f"{base_url}/report"

    response = requests.get(url=url, headers=auth_headers)

    assert response.status_code == 200

def test_update_report(_report_id, auth_headers):
    url = f"{base_url}/report/{_report_id}"

    data = {
        "title":"Updated Title"
    }
    response = requests.put(url=url, json=data, headers=auth_headers)

    assert response.status_code == 202
    assert response.json()['title'] == data['title']

def test_delete_report(_report_id, auth_headers):
    url = f"{base_url}/report/{_report_id}"

    response = requests.delete(url=url, headers=auth_headers)

    assert response.status_code == 200
   