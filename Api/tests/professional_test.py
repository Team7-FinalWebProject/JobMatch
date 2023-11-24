import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)


valid_professional = {"username": "testuser1", "password": f"{valid_password}"}
proftoken = client.post("/login/professionals", json=valid_professional).json()["token"]
valid_prof_info = {
  "first_name": "string",
  "last_name": "string",
  "summary": "string",
  "address": "string",
  "picture": "string"
}


def test_edit_professional_info_valid_info_200():
    response = client.put("/professional/1", json=valid_prof_info, headers={"X-Token": proftoken})
    assert response.status_code == 200
    assert response.json()["first_name"] == valid_prof_info["first_name"]
    assert response.json()["last_name"] == valid_prof_info["last_name"]
    assert response.json()["summary"] == valid_prof_info["summary"]
    assert response.json()["address"] == valid_prof_info["address"]
    assert response.json()["picture"] == valid_prof_info["picture"]


