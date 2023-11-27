import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()


valid_message = {
    "content": "string"
}

invalid_message = {
    "":1
}

# MESSAGE TESTS MIGHT FAIL IF NO DATA IN DB

def test_view_user_messages_valid_data_200(proftoken):
    response = client.get("/messages/testuser2", headers={"X-Token": proftoken})
    assert response.status_code == 200


def test_view_user_messages_invalid_data_401(proftoken):
    response = client.get("/messages/testuser2", headers={})
    assert response.status_code == 401

def test_view_user_messages_invalid_data_404(proftoken):
    response = client.get("/messages/asdasfasfr", headers={"X-Token": proftoken})
    assert response.status_code == 404


def test_send_message_valid_data_200(proftoken):
    response = client.post("/messages/testuser2", json=valid_message, headers={"X-Token": proftoken})
    assert response.status_code == 200
    response = response.json()
    assert "content" in response[0]


def test_send_message_invalid_data_401(proftoken):
    response = client.post("/messages/testuser2", headers={})
    assert response.status_code == 401


def test_send_message_invalid_data_404(proftoken):
    response = client.post("/messages/asdasfasfr", headers={"X-Token": proftoken})
    assert response.status_code == 404