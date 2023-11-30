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



def test_edit_company_info_valid_info_200(companytoken):
    response = client.put("/companies/info", json=valid_comp_info, headers={"X-Token": companytoken})
    assert response.status_code == 200
    assert response.json()["name"] == valid_comp_info["name"]
    assert response.json()["description"] == valid_comp_info["description"]
    assert response.json()["address"] == valid_comp_info["address"]
    assert response.json()["picture"] == valid_comp_info["picture"]



def test_edit_company_info__no_token_401(companytoken):
    response = client.put("/companies/info", json=valid_comp_info)
    assert response.status_code == 401



