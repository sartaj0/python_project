import pytest
from app import app

@pytest.fixture()
def app():
	app.config.update({"TESTING": True})
	return app 


@pytest.fixture("module")
def client(app):
    return app.test_client()

@pytest
def test_getusers(client):
	response = client.get("/users")
	assert response.status_code == 200