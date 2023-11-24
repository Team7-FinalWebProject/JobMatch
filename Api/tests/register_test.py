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

def test_register_professional_invalid_password_422():
    response = client.post("/register/professionals", json=invalid_professional_password)
    assert response.status_code == 422


def test_register_company_invalid_password_422():
    response = client.post("/register/companies", json=invalid_comp_password)
    assert response.status_code == 422


def test_register_professional_valid_200():
    response = client.post("/register/professionals", json=valid_professional_password)
    assert response.status_code == 200
    response = response.json()
    assert "username" in response
    assert "first_name" in response
    assert "last_name" in response
    assert "summary" in response


def test_register_company_valid_200():
    response = client.post("/register/companies", json=valid_company_password)
    assert response.status_code == 200
    response = response.json()
    assert "username" in response
    assert "company_name" in response
    assert "description" in response
    assert "address" in response

    