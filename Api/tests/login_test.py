import os
import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_login_professional_invalid_400(invalid_user):
    response = client.post("/login/professionals", json=invalid_user)
    assert response.status_code == 400

def test_login_companies_invalid_400(invalid_user):
    response = client.post("/login/companies", json=invalid_user)
    assert response.status_code == 400

def test_login_admins_invalid_400(invalid_user):
    response = client.post("/login/admins", json=invalid_user)
    assert response.status_code == 400

def test_login_professional_valid_200(valid_professional):
    response = client.post("/login/professionals", json=valid_professional)
    assert response.status_code == 200
    response = response.json()
    assert "token" in response
    assert len(response["token"]) > 0

def test_login_companies_valid_200(valid_company):
    response = client.post("/login/companies", json=valid_company)
    assert response.status_code == 200
    response = response.json()
    assert "token" in response
    assert len(response["token"]) > 0

def test_login_admins_valid_200(valid_admin):
    response = client.post("/login/admins", json=valid_admin)
    assert response.status_code == 200
    response = response.json()
    assert "token" in response
    assert len(response["token"]) > 0

def test_login_professional_invalid_username_400(invalid_username):
    response = client.post("/login/professionals", json=invalid_username)
    assert response.status_code == 400

def test_login_companies_invalid_username_400(invalid_username):
    response = client.post("/login/companies", json=invalid_username)
    assert response.status_code == 400

def test_login_admins_invalid_username_400(invalid_username):
    response = client.post("/login/admins", json=invalid_username)
    assert response.status_code == 400

def test_login_professional_invalid_password_400(invalid_prof_password):
    response = client.post("/login/professionals", json=invalid_prof_password)
    assert response.status_code == 400

def test_login_companies_invalid_password_400(invalid_comp_password):
    response = client.post("/login/companies", json=invalid_comp_password)
    assert response.status_code == 400

def test_login_admins_invalid_password_400(invalid_admin_password):
    response = client.post("/login/admins", json=invalid_admin_password)
    assert response.status_code == 400

def test_login_professional_invalid_admin_400(valid_admin):
    response = client.post("/login/professionals", json=valid_admin)
    assert response.status_code == 400

def test_login_companies_invalid_admin_400(valid_admin):
    response = client.post("/login/companies", json=valid_admin)
    assert response.status_code == 400

def test_login_companies_invalid_professional_400(valid_professional):
    response = client.post("/login/companies", json=valid_professional)
    assert response.status_code == 400

def test_login_admins_invalid_professional_400(valid_professional):
    response = client.post("/login/admins", json=valid_professional)
    assert response.status_code == 400

def test_login_professional_invalid_company_400(valid_company):
    response = client.post("/login/professionals", json=valid_company)
    assert response.status_code == 400

def test_login_admins_invalid_company_400(valid_company):
    response = client.post("/login/admins", json=valid_company)
    assert response.status_code == 400
