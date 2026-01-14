import pytest
import requests
from utils.config import BASE_API_URL


@pytest.mark.api
def test_get_users_returns_200_and_data():
    r = requests.get(f"{BASE_API_URL}/api/users?page=2", timeout=15)
    assert r.status_code == 200
    body = r.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@pytest.mark.api
def test_create_user_returns_201_and_id():
    payload = {"name": "Ekman", "job": "QA Automation"}
    r = requests.post(f"{BASE_API_URL}/api/users", json=payload, timeout=15)
    assert r.status_code == 201
    body = r.json()
    assert body["name"] == "Ekman"
    assert body["job"] == "QA Automation"
    assert "id" in body
