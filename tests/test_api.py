import pytest
from flask.testing import FlaskClient
from ..flaskr import app


@pytest.fixture(scope="function")
def client():
    app.config.update({"TESTING": True})

    return app.test_client()


def test_from_usd_to_cop(client: FlaskClient):
    response = client.post("/", json={"from": "USD", "to": "COP", "value": 3000})
    assert response.json == {"USD": 3000.0, "in COP": 12039990.0}


def test_from_cop_to_eur(client: FlaskClient):
    response = client.post("/", json={"from": "COP", "to": "EUR", "value": 5000})
    assert response.json == {"COP": 5000.0, "in EUR": 1.2}

def test_from_eur_to_eur(client: FlaskClient):
    response = client.post("/", json={"from": "EUR", "to": "EUR", "value": 200})
    assert response.json == {"EUR": 200.0, "in EUR": 200.0}
