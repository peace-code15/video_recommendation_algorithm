import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_feed_endpoint(client):
    response = client.get("/feed?username=1")
    assert response.status_code == 200
    assert "recommendations" in response.json
