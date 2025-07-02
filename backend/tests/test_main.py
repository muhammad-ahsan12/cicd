from fastapi.testclient import TestClient
from main import app  # Note: No 'backend.' prefix

client = TestClient(app)

def test_read_root():  # Must start with 'test_'
    response = client.get("/")
    assert response.status_code == 200