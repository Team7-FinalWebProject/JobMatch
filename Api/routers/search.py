from fastapi import APIRouter, Response, Header, Body
from services import search_service
from common.auth import user_or_401

##TODO: Temporary router, merge search router into professionals/companies when done
search_router = APIRouter(prefix='/search', tags=["Search Global"])
search_professional_router = APIRouter(prefix='/search', tags=["Search Professional"])
search_company_router = APIRouter(prefix='/search', tags=["Search Company"])

# --view company
@search_router.get('/company/{id}', tags=["Search Global"])
def view_approved_company(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_company_by_id(id)

# --view all companies (+filters)
@search_router.get('/companies', tags=["Search Global"])
def view_approved_companies(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_companies()

# --view professional
@search_router.get('/professional/{id}', tags=["Search Global"])
def view_approved_professional(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professional_by_id(id)

# --view all professionals (+filters)
@search_router.get('/professionals', tags=["Search Global"])
def view_approved_professionals(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professionals()

# --view company offer
@search_router.get('/company_offer/{id}', tags=["Search Global"])
def view_approved_company_offer(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_company_offer_by_id(id)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
@search_router.get('/company_offers', tags=["Search Global"])
def view_approved_company_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_company_offers(min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id)

# --view professional offer (hide hidden)
@search_router.get('/professional_offer/{id}', tags=["Search Global"])
def view_approved_professional_offer(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professional_offer_by_id(id)

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
@search_router.get('/professional_offers', tags=["Search Global"])
def view_approved_professional_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professional_offers(min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id)

@search_router.put('/propose_skills', tags=["Search Extra"])
def propose_skills(skills: list = Body(default=["Skill1", "Skill2"]), x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.propose_new_skills({s.capitalize():user.username for s in skills})


@search_router.post('/add_filter', tags=["Search Global"])
def save_filter(skill_filters:dict = Body(default={"Computers" : 1, "English": 1}), x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.add_webfilter(user.user_id, skill_filters)








##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
# ####Professional:
@search_professional_router.get('/professional_self_info', tags=["Search Professional"])
def view_approved_professional_self_info(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_self_info(user.id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_self_offer', tags=["Search Professional"])
def view_approved_hidden_professional_self_offer(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_self_offer_by_id(id, user.id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_self_offers', tags=["Search Professional"])
def view_approved_hidden_professional_self_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_self_offers(user.id, min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_company_offer', tags=["Search Professional"])
def view_approved_active_company_offer(id:int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_company_offer_by_id(id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_company_offers', tags=["Search Professional"])
def view_approved_active_company_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_company_offers(min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id) if user.__class__.__name__ == 'Professional' else None

##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
# ####Company:
@search_company_router.get('/company_self_info', tags=["Search Company"])
def view_approved_company_self_info(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_self_info(user.id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_self_offer', tags=["Search Company"])
def view_approved_archived_company_self_offer(id:int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_self_offer_by_id(id, user.id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_self_offers', tags=["Search Company"])
def view_approved_archived_company_self_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_self_offers(user.id, min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_professional_offer', tags=["Search Company"])
def view_approved_active_company_professional_offer(id:int,x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_professional_offer_by_id(id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_professional_offers', tags=["Search Company"])
def view_approved_active_company_professional_offers(min_salary: int = 0, max_salary: int = 1000000, filter_distance_from_latest: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_professional_offers(min_salary, max_salary, filter_distance_from_latest, salary_threshold_pct, allowed_missing_skills, user.user_id) if user.__class__.__name__ == 'Company' else None
