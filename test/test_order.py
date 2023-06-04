import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.mark.parametrize("test_order", ["banana", "apple", "orange"])
def test_post_order(test_order: str):
    response = client.post("/order", json={"order": test_order})
    assert response.status_code == 200
    assert response.json() == {"order": test_order}
