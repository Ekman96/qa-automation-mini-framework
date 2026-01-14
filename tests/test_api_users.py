import pytest
import requests
from utils.config import BASE_API_URL


@pytest.mark.api
def test_get_returns_200_and_json():
    r = requests.get(f"{BASE_API_URL}/get", params={"page": 2}, timeout=15)
    assert r.status_code == 200
    body = r.json()
    assert body["args"]["page"] == "2"


@pytest.mark.api
def test_post_returns_200_and_echoes_payload():
    payload = {"name": "Ekman", "job": "QA Automation"}
    r = requests.post(f"{BASE_API_URL}/post", json=payload, timeout=15)
    assert r.status_code == 200
    body = r.json()
    assert body["json"] == payload
