import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()

valid_professional = {"username": "testuser1", "password": f"{valid_password}"}
proftoken = client.post("/login/professionals", json=valid_professional).json()["token"]
valid_prof_info = {
  "first_name": "string",
  "last_name": "string",
  "summary": "string",
  "address": "string",
  "picture": "string"
}

valid_prof_offer_info = {
  "description": "string",
  "status": "string",
  "skills": {
    "English": [
      0,
      "Native"
    ]
  },
  "min_salary": 1000,
  "max_salary": 2000
}




def test_edit_professional_info_valid_info_200():
    response = client.put("/professionals/info", json=valid_prof_info, headers={"X-Token": proftoken})
    assert response.status_code == 200
    assert response.json()["first_name"] == valid_prof_info["first_name"]
    assert response.json()["last_name"] == valid_prof_info["last_name"]
    assert response.json()["summary"] == valid_prof_info["summary"]
    assert response.json()["address"] == valid_prof_info["address"]
    assert response.json()["picture"] == valid_prof_info["picture"]


def test_create_prof_offer_valid_info_200():
    response = client.post("/professionals/offer", json=valid_prof_offer_info, headers={"X-Token": proftoken})
    assert response.status_code == 200
    assert response.json()["description"] == valid_prof_offer_info["description"]
    assert response.json()["status"] == valid_prof_offer_info["status"]
    assert response.json()["skills"] == valid_prof_offer_info["skills"]
    assert response.json()["min_salary"] == valid_prof_offer_info["min_salary"]
    assert response.json()["max_salary"] == valid_prof_offer_info["max_salary"]


