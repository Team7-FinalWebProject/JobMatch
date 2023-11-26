import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()

valid_prof_info = {
  "first_name": "string",
  "last_name": "string",
  "summary": "string",
  "address": "string",
  "picture": None
}

valid_prof_offer_info = {
  "description": "string",
  "status": "active",
  "skills": {
    "English": [
      0,
      "Native"
    ]
  },
  "min_salary": 1000,
  "max_salary": 2000
}

invalid_prof_offer_info = {
  "description": "string",
  "status": "active",
  "skills": {
    "English": [
      0,
      "Native"
    ]
  },
  "min_salary": '',
  "max_salary": ''  
}

valid_offer_edit_info = {
  "chosen_company_offer_id": 1,
  "description": "string",
  "skills": {
  "English": [
      0,
      "Native"
    ]
  },
  "min_salary": 1000,
  "max_salary": 2000
}

invalid_offer_edit_info = {
  "chosen_company_offer_id": '',
  "skills": {
  "English": [
      0,
      "Native"
    ]
  },
  "min_salary": 1000,
  "max_salary": 2000
}


def test_edit_professional_info_valid_info_200(proftoken):
    response = client.put("/professionals/info", json=valid_prof_info, headers={"X-Token": proftoken})
    assert response.status_code == 200
    assert response.json()["first_name"] == valid_prof_info["first_name"]
    assert response.json()["last_name"] == valid_prof_info["last_name"]
    assert response.json()["summary"] == valid_prof_info["summary"]
    assert response.json()["address"] == valid_prof_info["address"]
    assert response.json()["picture"] == valid_prof_info["picture"]


def test_edit_professional_info__no_token_401(proftoken):
    response = client.put("/professionals/info", json=valid_prof_info)
    assert response.status_code == 401


def test_set_default_offer_valid_info_200(proftoken):
    response = client.put("/professionals/1/default_offer", headers={"X-Token": proftoken})
    assert response.status_code == 200


def test_set_default_offer_valid_info_401(proftoken):
    response = client.put("/professionals/1/default_offer", headers={})
    assert response.status_code == 401


def test_set_default_offer_valid_info_400(proftoken):
    response = client.put("/professionals/2/default_offer", headers={"X-Token": proftoken})
    assert response.status_code == 400


def test_create_prof_offer_valid_info_200(proftoken):
    response = client.post("/professionals/offer", json=valid_prof_offer_info, headers={"X-Token": proftoken})
    assert response.status_code == 200
    assert response.json()["description"] == valid_prof_offer_info["description"]
    assert response.json()["status"] == valid_prof_offer_info["status"]
    assert response.json()["skills"] == valid_prof_offer_info["skills"]
    assert response.json()["min_salary"] == valid_prof_offer_info["min_salary"]
    assert response.json()["max_salary"] == valid_prof_offer_info["max_salary"]


def test_create_prof_offer_invalid_data_422(proftoken):
    response = client.post("/professionals/offer", json=invalid_prof_offer_info, headers={"X-Token": proftoken})
    assert response.status_code == 422


def test_create_prof_offer_401():
    response = client.post("/professionals/offer", json=valid_prof_offer_info, headers={})
    assert response.status_code == 401


def test_edit_prof_offer_valid_data_200(proftoken):
    response = client.put("/professionals/1/edit_offer", json=valid_offer_edit_info, headers={"X-Token": proftoken})
    assert response.status_code == 200
    assert response.json()["description"] == valid_offer_edit_info["description"]
    assert response.json()["chosen_company_offer_id"] == valid_offer_edit_info["chosen_company_offer_id"]
    assert response.json()["skills"] == valid_offer_edit_info["skills"]
    assert response.json()["min_salary"] == valid_offer_edit_info["min_salary"]
    assert response.json()["max_salary"] == valid_offer_edit_info["max_salary"]


def test_edit_prof_offer_invalid_data_422(proftoken):
    response = client.put("/professionals/1/edit_offer", json=invalid_offer_edit_info, headers={"X-Token": proftoken})
    assert response.status_code == 422


def test_edit_prof_offer_401():
    response = client.put("/professionals/1/edit_offer", json=valid_offer_edit_info)
    assert response.status_code == 401