from fastapi.testclient import TestClient
from backend.main import app  # Ensure this import works

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200