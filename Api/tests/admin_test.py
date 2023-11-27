import os
import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()

change_config_valid_info = {
  "static_skills": false,
  "min_level": 0,
  "max_level": 10
}


def test_view_unapproved_company_valid_data_200(admintoken):
    response = client.get("/admin/company/1", headers={"X-Token": admintoken})
    assert response.status_code == 200
    assert response.json() == "null"
    
def test_view_unapproved_company_no_token_401(admintoken):
    response = client.get("/admin/company/1", headers={})
    assert response.status_code == 401

def test_view_unapproved_companies_valid_data_200(admintoken):
    response = client.get("/admin/companies", headers={"X-Token": admintoken})
    assert response.status_code == 200
    assert response.json() == "[]"
    
def test_view_unapproved_companies_no_token_401(admintoken):
    response = client.get("/admin/companies", headers={})
    assert response.status_code == 401

def test_view_unapproved_professional_valid_data_200(admintoken):
    response = client.get("/admin/professional/1", headers={"X-Token": admintoken})
    assert response.status_code == 200
    assert response.json() == "null"
   
def test_view_unapproved_professional_no_token_401(admintoken):
    response = client.get("/admin/professional/1", headers={})
    assert response.status_code == 401

def test_view_unapproved_professionals_valid_data_200(admintoken):
    response = client.get("/admin/professionals", headers={"X-Token": admintoken})
    assert response.status_code == 200
    response = response.json()
    assert "id" in response[0]
    assert "username" in response[0]
    assert "default_offer_id" in response[0]
    assert "first_name" in response[0]
    assert "last_name" in response[0]
    assert "summary" in response[0]
    assert "address" in response[0]
    assert "picture" in response[0]
    assert "status" in response[0]

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbnVzZXIiLCJpc3N1ZWQiOiIyMDIzLTExLTI3IDEyOjIyOjEwLjI0MDU0NyJ9.joDpdtiO51VEPAlq1YEtToZK2uRmm4NAts98HQwaMSE

def test_view_unapproved_professionals_no_token_401(admintoken):
    response = client.get("/admin/professionals", headers={})
    assert response.status_code == 401
    

def test_view_config_valid_data_200(admintoken):
    response = client.get("/admin/config", headers={"X-Token": admintoken})
    assert response.status_code == 200
    response = response.json()
    assert "static_skills" in response[0]
    assert "min_level" in response[0]
    assert "max_level" in response[0]
    assert "baseline_skills" in response[0]
    assert "approved_skills" in response[0]
    assert "pending_approval_skills" in response[0]


def test_view_config_no_token_401(admintoken):
    response = client.get("/admin/config", headers={})
    assert response.status_code == 401
    

def test_change_config_valid_data_200(admintoken):
    response = client.patch("/admin/config", json=change_config_valid_info, headers={"X-Token": admintoken})
    assert response.status_code == 200
    

def test_change_config_no_token_401(admintoken):
    response = client.patch("/admin/config", json=change_config_valid_info, headers={})
    assert response.status_code == 401
    