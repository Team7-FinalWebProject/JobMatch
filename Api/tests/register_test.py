import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)

valid_password = os.getenv('userpassword')
load_dotenv()



invalid_professional_password = {
  "username": "X_6issk5EHKov7hri1Vn",
  "password": "stringst",
  "first_name": "string",
  "last_name": "string",
  "address": "string",
  "summary": "string",
  "picture": "string"
}

invalid_comp_password =  {
  "username": "dLvUmTeU",
  "password": "stringst",
  "company_name": "string",
  "description": "string",
  "address": "string",
  "picture": "string"
}

valid_professional_password = {
  "username": "X_6issk5EHKov7hri1Vn",
  "password": f"{valid_password}",
  "first_name": "string",
  "last_name": "string",
  "address": "string",
  "summary": "string",
  "picture": "string"
}

valid_company_password = {
  "username": "dLvUmTeU",
  "password": f"{valid_password}",
  "company_name": "string",
  "description": "string",
  "address": "string",
  "picture": "string"
}

expected_company_data = {
        "username": "dLvUmTeU",
        "company_name": "string",
        "description": "string",
        "address": "string"
}

expected_prof_data = {
        "username": "X_6issk5EHKov7hri1Vn",
        "first_name": "string",
        "last_name": "string",
        "summary": "string"
}


def test_register_professional_invalid_password_422():
    response = client.post("/register/professionals", json=invalid_professional_password)
    assert response.status_code == 422


def test_register_company_invalid_password_422():
    response = client.post("/register/companies", json=invalid_comp_password)
    assert response.status_code == 422


def test_register_professional_valid_200():
    response = client.post("/register/professionals", json=valid_professional_password)
    assert response.status_code == 200
    assert response.json()["username"] == expected_prof_data["username"]
    assert response.json()["first_name"] == expected_prof_data["first_name"]
    assert response.json()["last_name"] == expected_prof_data["last_name"]
    assert response.json()["summary"] == expected_prof_data["summary"]


def test_register_company_valid_200():
    response = client.post("/register/companies", json=valid_company_password)
    assert response.status_code == 200
    assert response.json()["username"] == expected_company_data["username"]
    assert response.json()["company_name"] == expected_company_data["company_name"]
    assert response.json()["description"] == expected_company_data['description']
    assert response.json()["address"] == expected_company_data["address"]

    