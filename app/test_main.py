from fastapi.testclient import TestClient
import app.config as cfg
from .main import app

client = TestClient(app)

data = {
    "remember": cfg.MESSAGE
}

def test_get_all():
    response = client.get("/rates", json=data)
    assert response.status_code == 200


def test_get_all_message():
    response = client.get("/message", json=data)
    assert response.status_code == 200
    assert response.json() == data
    
