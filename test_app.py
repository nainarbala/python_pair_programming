import pytest

from app import app


@pytest.fixture

def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_simple_interest_success(client):
    response = client.post(
        "/simple-interest",
        json={"principal": 1000, "rate": 5, "time": 2},
    )

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "principal": 1000.0,
        "rate": 5.0,
        "time": 2.0,
        "simple_interest": 100.0,
    }


def test_simple_interest_missing_field(client):
    response = client.post(
        "/simple-interest",
        json={"principal": 1000, "rate": 5},
    )

    assert response.status_code == 400
    assert response.is_json
    assert "Missing required field(s): time." in response.get_json()["error"]


def test_simple_interest_invalid_type(client):
    response = client.post(
        "/simple-interest",
        json={"principal": "abc", "rate": 5, "time": 2},
    )

    assert response.status_code == 400
    assert response.is_json
    assert "principal must be numeric." in response.get_json()["error"]


def test_simple_interest_negative_value(client):
    response = client.post(
        "/simple-interest",
        json={"principal": -1000, "rate": 5, "time": 2},
    )

    assert response.status_code == 400
    assert response.is_json
    assert "principal must be non-negative." in response.get_json()["error"]
