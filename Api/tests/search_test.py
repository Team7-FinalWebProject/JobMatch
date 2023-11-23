import os
import pytest
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from main import app

client = TestClient(app)
valid_password = os.getenv('userpassword')
load_dotenv()

valid_admin = {"username": "adminuser", "password": f"{valid_password}"}
valid_professional = {"username": "testuser1", "password": f"{valid_password}"}
valid_company = {"username": "testuser4", "password": f"{valid_password}"}
proftoken = client.post("/login/professionals", json=valid_professional).json()["token"]
companytoken = client.post("/login/companies", json=valid_company).json()["token"]
admintoken = client.post("/login/admins", json=valid_admin).json()["token"]

def test_get_company_id_valid_company_200():
    response = client.get("/search/company/1", headers={"X-Token": companytoken})
    assert response.status_code == 200
    assert response.json() == "JobUtopia"

def test_get_company_id_valid_prof_200():
    response = client.get("/search/company/1", headers={"X-Token": proftoken})
    assert response.status_code == 200
    assert response.json() == "JobUtopia"

def test_get_company_id_valid_admin_200():
    response = client.get("/search/company/1", headers={"X-Token": admintoken})
    assert response.status_code == 200
    assert response.json() == "JobUtopia"

def test_get_company_id_invalid_token_400():
    response = client.get("/search/company/1", headers={"X-Token": b"hailhydra"})
    assert response.status_code == 400
    assert response.json() == "JobUtopia"





# # --view company
# @search_router.get('/company/{id}', tags=["Search Global"])
# def view_approved_company(id: int, x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_company_by_id(id)

# # --view all companies (+filters)
# @search_router.get('/companies', tags=["Search Global"])
# def view_approved_companies(x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_companies()

# # --view professional
# @search_router.get('/professional/{id}', tags=["Search Global"])
# def view_approved_professional(id: int, x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_professional_by_id(id)

# # --view all professionals (+filters)
# @search_router.get('/professionals', tags=["Search Global"])
# def view_approved_professionals(x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_professionals()

# # --view company offer
# @search_router.get('/company_offer/{id}', tags=["Search Global"])
# def view_approved_company_offer(id: int, x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_company_offer_by_id(id)

# # --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
# @search_router.get('/company_offers', tags=["Search Global"])
# def view_approved_company_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_company_offers(min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id)

# # --view professional offer (hide hidden)
# @search_router.get('/professional_offer/{id}', tags=["Search Global"])
# def view_approved_professional_offer(id: int, x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_professional_offer_by_id(id)

# # --view all professional offers (self, self=professional, filters: active/inactive)
# # --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
# @search_router.get('/professional_offers', tags=["Search Global"])
# def view_approved_professional_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.search_get_professional_offers(min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id)

# @search_router.put('/propose_skills', tags=["Search Extra"])
# def propose_skills(skills: list = Body(default=["Skill1", "Skill2"]), x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.propose_new_skills({s.capitalize():user.username for s in skills})


# @search_router.post('/add_filter', tags=["Search Global"])
# def save_filter(skill_filters:dict = Body(default={"Computers" : 1, "English": 1}), x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.add_webfilter(user.user_id, skill_filters)

