import os
import pytest
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from main import app

client = TestClient(app)

@pytest.fixture
def valid_tokens(companytoken,proftoken,admintoken):
    return (companytoken,proftoken,admintoken)

@pytest.fixture
def invalid_tokens():
    return ("hailhydra",b"hailhydra")














####-----------------COMPANY_BY_ID----------------------####
def test_get_company_by_id_invalid_token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/company/1", headers={"X-Token": token})
        assert response.status_code == 401

@pytest.mark.parametrize("id,value", [
    (1,"Pepsi"),
    (2,"Steam"),
    (3,"Avid"),
])
def test_get_company_by_id_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company/{id}", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()["name"] == value

@pytest.mark.parametrize("id", [
    99999,
    -10,
    0,
    '?',
    '/////',
    '/?=?-./',
    '${jndi:ldap://google.com/}',
    '0/1/2/3/4/5',
])
def test_get_company_by_id_invalid_path_404(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company/{id}", headers={"X-Token": token})
        assert response.status_code == 404


@pytest.mark.parametrize("id", [
    "Pepsi",
    0.5,
])
def test_get_company_by_id_invalid_id_422(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company/{id}", headers={"X-Token": token})
        assert response.status_code == 422























####-----------------COMPANIES----------------------####
def test_get_companies_invalid_str_token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/companies", headers={"X-Token": token})
        assert response.status_code == 401


@pytest.mark.parametrize("id,value", [
    (1,"Pepsi"),
    (2,"Steam"),
    (3,"Avid"),
])
def test_get_companies_no_filter_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/companies", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()[id-1]["name"] == value


def test_get_companies_valid_filter_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/companies", headers={"X-Token": token})
        assert response.status_code == "write the test"


def test_get_companies_invalid_filter_invalid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/companies", headers={"X-Token": token})
        assert response.status_code == "write the test"




























####-----------------PROFESSIONAL_BY_ID----------------------####
def test_get_professional_by_id_invalid__token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/professional/1", headers={"X-Token": token})
        assert response.status_code == 401

@pytest.mark.parametrize("id,value", [
    (1,"John"),
    (2,"Michael"),
])
def test_get_professional_by_id_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional/{id}", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()["first_name"] == value

@pytest.mark.parametrize("id,value", [
    (3,"William"),
])
def test_get_professional_by_id_unapproved_404(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional/{id}", headers={"X-Token": token})
        assert response.status_code == 404



@pytest.mark.parametrize("id", [
    99999,
    -10,
    0,
    '?',
    '/////',
    '/?=?-./',
    '${jndi:ldap://google.com/}',
    '0/1/2/3/4/5',
])
def test_get_professional_by_id_invalid_path_404(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional/{id}", headers={"X-Token": token})
        assert response.status_code == 404




@pytest.mark.parametrize("id", [
    "Pepsi",
    0.5,
])
def test_get_professional_by_id_invalid_id_422(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional/{id}", headers={"X-Token": token})
        assert response.status_code == 422





























####-----------------PROFESSIONALS----------------------####
def test_get_professionals_invalid_str_token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/professionals", headers={"X-Token": token})
        assert response.status_code == 401


@pytest.mark.parametrize("id,value", [
    (1,"John"),
    (2,"Michael"),
    (3,"William"),
])
def test_get_professionals_no_filter_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professionals", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()[id-1]["first_name"] == value


def test_get_professionals_valid_filter_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professionals", headers={"X-Token": token})
        assert response.status_code == "write the test"


def test_get_professionals_invalid_filter_invalid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professionals", headers={"X-Token": token})
        assert response.status_code == "write the test"



























####-----------------COMPANY_OFFER_BY_ID----------------------####
def test_get_company_offer_by_id_invalid_token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/company_offer/1", headers={"X-Token": token})
        assert response.status_code == 401

@pytest.mark.parametrize("id,value", [
    (1,3000),
    (2,2500),
    (3,1500),
])
def test_get_company_offer_by_id_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company_offer/{id}", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()["min_salary"] == value

@pytest.mark.parametrize("id", [
    99999,
    -10,
    0,
    '?',
    '/////',
    '/?=?-./',
    '${jndi:ldap://google.com/}',
    '0/1/2/3/4/5',
])
def test_get_company_offer_by_id_invalid_path_404(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company_offer/{id}", headers={"X-Token": token})
        assert response.status_code == 404


@pytest.mark.parametrize("id", [
    "Pepsi",
    0.5,
])
def test_get_company_offer_by_id_invalid_id_422(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company_offer/{id}", headers={"X-Token": token})
        assert response.status_code == 422






























####-----------------COMPANY_OFFERS----------------------####
def test_get_company_offers_invalid__token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/company_offers", headers={"X-Token": token})
        assert response.status_code == 401

@pytest.mark.parametrize("id,value", [
    (1,3000),
    (2,2500),
    (3,1500),
])
def test_get_company_offers_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company_offers", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()[id-1]["min_salary"] == value

def test_get_company_offers_valid_filter_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company_offers", headers={"X-Token": token})
        assert response.status_code == "write the test"


def test_get_company_offers_invalid_filter_invalid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/company_offers", headers={"X-Token": token})
        assert response.status_code == "write the test"






























####-----------------PROFESSIONAL_OFFER_BY_ID----------------------####
def test_get_professional_offer_by_id_invalid__token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/professional_offer/1", headers={"X-Token": token})
        assert response.status_code == 401

@pytest.mark.parametrize("id,value", [
    (1,3000),
    (2,2000),
])
def test_get_professional_offer_by_id_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional_offer/{id}", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()["min_salary"] == value


@pytest.mark.parametrize("id,value", [
    (3,1300),
])
def test_get_professional_offer_by_id_unapproved_404(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional_offer/{id}", headers={"X-Token": token})
        assert response.status_code == 404

@pytest.mark.parametrize("id", [
    99999,
    -10,
    0,
    '?',
    '/////',
    '/?=?-./',
    '${jndi:ldap://google.com/}',
    '0/1/2/3/4/5',
])
def test_get_professional_offer_by_id_invalid_path_404(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional_offer/{id}", headers={"X-Token": token})
        assert response.status_code == 404


@pytest.mark.parametrize("id", [
    "Pepsi",
    0.5,
])
def test_get_professional_offer_by_id_invalid_id_422(id,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional_offer/{id}", headers={"X-Token": token})
        assert response.status_code == 404






























####-----------------PROFESSIONAL_OFFERS----------------------####
def test_get_professional_offers_invalid__token_401(invalid_tokens):
    for token in invalid_tokens:
        response = client.get("/search/professional_offers", headers={"X-Token": token})
        assert response.status_code == 401

@pytest.mark.parametrize("id,value", [
    (1,3000),
    (2,2000),
])
def test_get_professional_offers_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional_offers", headers={"X-Token": token})
        assert response.status_code == 200
        assert response.json()[id-1]["min_salary"] == value

def test_get_professional_offers_valid_filter_valid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional_offers", headers={"X-Token": token})
        assert response.status_code == "write the test"


def test_get_professional_offers_invalid_filter_invalid_200(id,value,valid_tokens):
    for token in valid_tokens:
        response = client.get(f"/search/professional_offers", headers={"X-Token": token})
        assert response.status_code == "write the test"








####-----------------PROPOSE_SKILLS----------------------####


# @search_router.put('/propose_skills', tags=["Search Extra"])
# def propose_skills(skills: list = Body(default=["Skill1", "Skill2"]), x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.propose_new_skills({s.capitalize():user.username for s in skills})


@pytest.fixture
def dummy_skills():
    return ("Skill1", "Skill2")

@pytest.fixture
def duplicate_skills():
    return ("Skill1", "Skill1", "Skill1")

@pytest.fixture
def small_skills():
    return ("skill1", "skill2", "skill3")


def test_propose_skills_no_skills_returns_200(valid_tokens):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token})
        assert response.status_code == 200

def test_propose_skills_no_skills_returns_200_2nd(valid_tokens):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=[])
        assert response.status_code == 200

def test_propose_skills_no_skills_returns_200_3rd(valid_tokens,dummy_skills):
    for token in valid_tokens:
        response1 =client.put(f"/search/propose_skills", headers={"X-Token": token}, json=dummy_skills)
        response2 = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=dummy_skills)
        assert response1.status_code == response2.status_code == 200

def test_propose_skills_duplicate_skills_returns_200(valid_tokens, dummy_skills):
    for token in valid_tokens:
        response =client.put(f"/search/propose_skills", headers={"X-Token": token}, json=dummy_skills)
        assert response.status_code == 200

def test_propose_skills_adds_proposed_skills(valid_tokens, dummy_skills):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=dummy_skills)
        assert response.status_code == 200
    config = client.get(f"/admin/config", headers={"X-Token": valid_tokens[2]})
    for skill in dummy_skills:
        assert skill in config.json()["pending_approval_skills"]

def test_propose_skills_does_not_duplicate_skills(valid_tokens, duplicate_skills):
    for token in valid_tokens:
        client.put(f"/search/propose_skills", headers={"X-Token": token}, json=duplicate_skills)
    config = client.get(f"/admin/config", headers={"X-Token": valid_tokens[2]})
    pending_skills = config.json()["pending_approval_skills"]
    del pending_skills[duplicate_skills[0]]
    assert duplicate_skills[0] not in pending_skills


def test_propose_skills_capitalizes_skills(valid_tokens, small_skills):
    for token in valid_tokens:
        client.put(f"/search/propose_skills", headers={"X-Token": token}, json=small_skills)
    config = client.get(f"/admin/config", headers={"X-Token": valid_tokens[2]})
    pending_skills = config.json()["pending_approval_skills"]
    for skill in small_skills:
        assert skill.capitalize() in pending_skills


@pytest.mark.parametrize("skill", [
    "Pepsi",
    99999,
    '${jndi:ldap://google.com/}',
])
def test_propose_skills_invalid_skills_422(valid_tokens, skill):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=skill)
    assert response.status_code == 422
    

class invalid_skills:
    skills = [
    (-10,),
    ("-10",),
    ("1",),
    (1,),
    (")",),
    ("?",),
    (">",),
    (".",),
    ("/",),
    ('${jndi:ldap://google.com/}',),]

    def return_invalid_skill(self, id):
        return self.skills[id]


def test_propose_skills_invalid_skills_422_2nd(valid_tokens):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=("-10",))
    assert response.status_code == 422
    

def test_propose_skills_invalid_skills_422_3rd(valid_tokens):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=(-10,))
    assert response.status_code == 422
    
def test_propose_skills_invalid_skills_422_4th(valid_tokens):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=(1,))
    assert response.status_code == 422
    

def test_propose_skills_invalid_skills_422_5th(valid_tokens):
    for token in valid_tokens:
        response = client.put(f"/search/propose_skills", headers={"X-Token": token}, json=("$",))
    assert response.status_code == 422
    
























####-----------------ADD_FILTER----------------------####
# @search_router.post('/add_filter', tags=["Search Global"])
# def save_filter(skill_filters:dict = Body(default={"Computers" : 1, "English": 1}), x_token: str = Header()):
#     user = user_or_error(x_token)
#     return search_service.add_webfilter(user.user_id, skill_filters)




@pytest.fixture
def dummy_filter():
    return {"Linguistics" : 1, "Automata Theory": 3}


@pytest.fixture
def small_filter():
        return {"linguistics" : 1, "automata Theory": 3}


def test_add_filter_no_filter_returns_200(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token})
        assert response.status_code == 200

def test_add_filter_no_filter_returns_200_2nd(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=[])
        assert response.status_code == 200

        
def test_add_filter_adds_filter(valid_tokens, dummy_filter):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=dummy_filter)
        assert response.status_code == 200
        saved_filters = client.get(f"/search/filter", headers={"X-Token": token})
        assert dummy_filter == saved_filters[0]

def test_add_filter_capitalizes_filter(valid_tokens, small_filter):
    for token in valid_tokens:
        client.post(f"/search/add_filter", headers={"X-Token": token}, json=small_filter)
        saved_filters = client.get(f"/search/filter", headers={"X-Token": token})
        for key in small_filter:
            small_filter[key.capitalize()] = small_filter[key]
            small_filter.pop(key)
        assert small_filter == saved_filters[0]


@pytest.mark.parametrize("filter", [
    "Pepsi",
    99999,
    '${jndi:ldap://google.com/}',
])
def test_add_filter_invalid_skills_422(valid_tokens, filter):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=filter)
    assert response.status_code == 422
    

class invalid_filters:
    filters = [
    (-10,),
    ("-10",),
    ("1",),
    (1,),
    (")",),
    ("?",),
    (">",),
    (".",),
    ("/",),
    ('${jndi:ldap://google.com/}',),]

    def return_invalid_filter(self, id):
        return self.filters[id]


def test_add_filter_invalid_filters_422_2nd(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=("-10",))
    assert response.status_code == 422
    

def test_add_filter_invalid_filters_422_3rd(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=(-10,))
    assert response.status_code == 422
    
def test_add_filter_invalid_filters_422_4th(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=(1,))
    assert response.status_code == 422
    

def test_add_filter_invalid_filters_422_5th(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=("$",))
    assert response.status_code == 422
    

def test_add_filter_invalid_filters_422_6th(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json=("English", "French"))
    assert response.status_code == 422
    


def test_add_filter_invalid_filters_422_7th(valid_tokens):
    for token in valid_tokens:
        response = client.post(f"/search/add_filter", headers={"X-Token": token}, json={"English" : "English", "French" : "French"})
    assert response.status_code == 422
    


