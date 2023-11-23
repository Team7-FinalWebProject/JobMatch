import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()

invalid_user = {"username": "EFrQjeqVSwyPx_t6O", "password": "stringst"}
invalid_username = {"username": "EFrQjeqVSwyPx_t6O", "password": f"{valid_password}"}
invalid_admin_password = {"username": "adminuser", "password": "stringst"}
invalid_prof_password = {"username": "testuser1", "password": "stringst"}
invalid_comp_password =  {"username": "testuser4", "password": "stringst"}
valid_admin = {"username": "adminuser", "password": f"{valid_password}"}
valid_professional = {"username": "testuser1", "password": f"{valid_password}"}
valid_company = {"username": "testuser4", "password": f"{valid_password}"}

def test_login_professional_invalid_400():
    response = client.post("/login/professionals", json=invalid_user)
    assert response.status_code == 400

def test_login_companies_invalid_400():
    response = client.post("/login/companies", json=invalid_user)
    assert response.status_code == 400

def test_login_admins_invalid_400():
    response = client.post("/login/admins", json=invalid_user)
    assert response.status_code == 400

def test_login_professional_valid_200():
    response = client.post("/login/professionals", json=valid_professional)
    assert response.status_code == 200
    response = response.json()
    assert "token" in response
    assert len(response["token"]) > 0

def test_login_companies_valid_200():
    response = client.post("/login/companies", json=valid_company)
    assert response.status_code == 200
    response = response.json()
    assert "token" in response
    assert len(response["token"]) > 0

def test_login_admins_valid_200():
    response = client.post("/login/admins", json=valid_admin)
    assert response.status_code == 200
    response = response.json()
    assert "token" in response
    assert len(response["token"]) > 0

def test_login_professional_invalid_username_400():
    response = client.post("/login/professionals", json=invalid_username)
    assert response.status_code == 400

def test_login_companies_invalid_username_400():
    response = client.post("/login/companies", json=invalid_username)
    assert response.status_code == 400

def test_login_admins_invalid_username_400():
    response = client.post("/login/admins", json=invalid_username)
    assert response.status_code == 400

def test_login_professional_invalid_password_400():
    response = client.post("/login/professionals", json=invalid_prof_password)
    assert response.status_code == 400

def test_login_companies_invalid_password_400():
    response = client.post("/login/companies", json=invalid_comp_password)
    assert response.status_code == 400

def test_login_admins_invalid_password_400():
    response = client.post("/login/admins", json=invalid_admin_password)
    assert response.status_code == 400

def test_login_professional_invalid_admin_400():
    response = client.post("/login/professionals", json=valid_admin)
    assert response.status_code == 400

def test_login_companies_invalid_admin_400():
    response = client.post("/login/companies", json=valid_admin)
    assert response.status_code == 400

def test_login_companies_invalid_professional_400():
    response = client.post("/login/companies", json=valid_professional)
    assert response.status_code == 400

def test_login_admins_invalid_professional_400():
    response = client.post("/login/admins", json=valid_professional)
    assert response.status_code == 400

def test_login_professional_invalid_company_400():
    response = client.post("/login/professionals", json=valid_company)
    assert response.status_code == 400

def test_login_admins_invalid_company_400():
    response = client.post("/login/admins", json=valid_company)
    assert response.status_code == 400
