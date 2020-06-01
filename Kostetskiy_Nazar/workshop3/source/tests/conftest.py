import pytest
from app import app


@pytest.fixture(autouse=True)
def test_app():
    with app.test_request_context():
        yield app


@pytest.fixture
def test_client(test_app):
    test_app.testing = True
    return test_app.test_client()

