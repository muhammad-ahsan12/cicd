from fastapi.testclient import TestClient
from main import app  # Remove "backend." prefix

client = TestClient(app)

def test_read_root():  # Fix typo (was test_read.root)
    response = client.get("/")
    assert response.status_code == 200