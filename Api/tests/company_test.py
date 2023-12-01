import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()

valid_comp_info = {
  "name": "DSK",
  "description": "remote",
  "address": "stfs",
  "picture": "string"
}


valid_comp_offer_info = {
  "requirements": {
    "English": [
      9,
      "Beginner"
    ]
  },
  "min_salary": 1000,
  "max_salary": 25000
}

invalid_comp_offer_info = {
  "requirements": {
    "English": [
      9,
      "Beginner"
    ]
  },
  "min_salary": "",
  "max_salary": ""
}



valid_offer_edit_info = {
  "id": 0,
  "company_id": 0,
  "chosen_professional_offer_id": 0,
  "status": "active",
  "requirements": {
    "Python": [
      3,
      "Expert"
    ]
  },
  "min_salary": 1000,
  "max_salary": 4000
}


invalid_offer_edit_info = {
  "id": 0,
  "company_id": 0,
  "chosen_professional_offer_id": 0,
  "status": "string",
  "requirements": {
    "Python": [
      3,
      "Expert"
    ]
  },
  "min_salary": 1000,
  "max_salary": 4000
}



def test_edit_company_info_valid_info_200(companytoken):
    response = client.put("/companies/info", json=valid_comp_info, headers={"X-Token": companytoken})
    assert response.status_code == 200
    assert response.json()["name"] == valid_comp_info["name"]
    assert response.json()["description"] == valid_comp_info["description"]
    assert response.json()["address"] == valid_comp_info["address"]
    assert response.json()["picture"] == valid_comp_info["picture"]



def test_edit_company_info_no_token_401(companytoken):
    response = client.put("/companies/info", json=valid_comp_info, headers={})
    assert response.status_code == 401




def test_create_company_offer_valid_info_200(companytoken):
    response = client.post("/companies/create_offer", json=valid_comp_offer_info, headers={"X-Token": companytoken})
    assert response.status_code == 200
    assert response.json()["requirements"] == valid_comp_offer_info["requirements"]
    assert response.json()["min_salary"] == valid_comp_offer_info["min_salary"]
    assert response.json()["max_salary"] == valid_comp_offer_info["max_salary"]


def test_create_company_offer_invalid_data_422(companytoken):
    response = client.post("/companies/create_offer", json=invalid_comp_offer_info, headers={"X-Token": companytoken})
    assert response.status_code == 422


def test_create_company_offer_no_token_401():
    response = client.post("/companies/create_offer", json=invalid_comp_offer_info, headers={})
    assert response.status_code == 401



def test_edit_comp_offer_valid_data_200(companytoken):
    response = client.put("/companies/1/edit_offer", json=valid_offer_edit_info, headers={"X-Token": companytoken})
    assert response.status_code == 200
    assert response.json()["status"] == valid_offer_edit_info["status"]
    assert response.json()["requirements"] == valid_offer_edit_info["requirements"]
    assert response.json()["min_salary"] == valid_offer_edit_info["min_salary"]
    assert response.json()["max_salary"] == valid_offer_edit_info["max_salary"]


def test_edit_comp_offer_wrong_status_400(companytoken):
    response = client.put("/companies/1/edit_offer", json=invalid_offer_edit_info, headers={"X-Token": companytoken})
    assert response.status_code == 400


def test_edit_comp_offer_401():
    response = client.put("/companies/1/edit_offer", json=valid_offer_edit_info)
    assert response.status_code == 401
    



def test_send_match_request_valid_data_200(companytoken):
    response = client.post("/companies/1/1/request", headers={"X-Token": companytoken})
    assert response.status_code == 200


def test_send_match_request_invalid_data_500(companytoken):
    response = client.post("/companies/2/1/request", headers={"X-Token": companytoken})
    assert response.status_code == 500


def test_send_match_request_invalid_data_401(companytoken):
    response = client.post("/companies/1/1/request", headers={})
    assert response.status_code == 401


def test_send_match_request_invalid_data_404(companytoken):
    response = client.post("/companies/1/-1/request", headers={"X-Token": companytoken})
    assert response.status_code == 404





def test_match_valid_data_200(companytoken):
    response = client.post("/companies/match?offer_id=1&prof_offer_id=1", headers={"X-Token": companytoken})
    assert response.status_code == 200


def test_match_invalid_data_401(companytoken):
    response = client.post("/companies/match?offer_id=1&prof_offer_id=1", headers={})
    assert response.status_code == 401


def test_match_invalid_data_403(companytoken):
    response = client.post("/companies/match?offer_id=3&prof_offer_id=1", headers={"X-Token": companytoken})
    assert response.status_code == 403
    

