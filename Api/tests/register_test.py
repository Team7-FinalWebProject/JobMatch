import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()

invalid_prof = {"username": "EFrQjeqVSwyPx_t6O", 
                "password": "stringst", "first_name": "1POJVUPQ[]",
                 "last_name": "poidfnu1", "address": "", "summary": "",
                  "picture": ""}
invalid_comp = {"username": "EFrQjeqVSwyPx_t6O", "password": "stringst",
                "company_name": "namename", "description": "1231dfaga",
                "address": "", "picture": ""}
valid_prof = {"username": "testuser9", "password": f"{valid_password}",
              "first_name": "Ivan", "last_name": "Ivanov", "address": "Sofia, BG",
              "summary": "This is my summary", "picture": ""}


# invalid_username = {"username": "EFrQjeqVSwyPx_t6O", "password": f"{valid_password}"}
# invalid_admin_password = {"username": "adminuser", "password": "stringst"}
# invalid_prof_password = {"username": "testuser1", "password": "stringst"}
# invalid_comp_password =  {"username": "testuser4", "password": "stringst"}
# valid_admin = {"username": "adminuser", "password": f"{valid_password}"}
# valid_professional = {"username": "testuser1", "password": f"{valid_password}"}
# valid_company = {"username": "testuser4", "password": f"{valid_password}"}


def test_register_professional_invalid_422():
    response = client.post('/register/professionals', json=invalid_prof)
    assert response.status_code == 422

def test_register_company_invalid_422():
    response = client.post('/register/companies', json=invalid_comp)
    assert response.status_code == 422

def test_register_professional_valid_200():
    response = client.post('/register/professionals', json=valid_prof)
    assert response.status_code == 200
    result = response.json()
    assert valid_prof["first_name"] in result
    assert valid_prof["last_name"] in result
    assert valid_prof['summary'] in result
