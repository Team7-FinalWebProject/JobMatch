from fastapi import APIRouter, Response, Header, Body
from services import search_service
from common.auth import user_or_error, admin_or_error

##TODO: Temporary router, merge search router into professionals/companies when done
search_router = APIRouter(prefix='/search', tags=["Search Global"])
search_professional_router = APIRouter(prefix='/professionals', tags=["Professional"])
search_company_router = APIRouter(prefix='/companies', tags=["Companies"])
search_admin_router = APIRouter(prefix='/admin', tags=["Admin"])

# --view company
@search_router.get('/company/{id}', tags=["Search Global"])
def view_approved_company(id: int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_company_by_id(id)

# --view all companies (+filters)
@search_router.get('/companies', tags=["Search Global"])
def view_approved_companies(x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_companies()

# --view professional
@search_router.get('/professional/{id}', tags=["Search Global"])
def view_approved_professional(id: int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_professional_by_id(id)

# --view all professionals (+filters)
@search_router.get('/professionals', tags=["Search Global"])
def view_approved_professionals(x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_professionals()

# --view company offer
@search_router.get('/company_offer/{id}', tags=["Search Global"])
def view_approved_company_offer(id: int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_company_offer_by_id(id)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
@search_router.get('/company_offers', tags=["Search Global"])
def view_approved_company_offers(min_salary: int = 0, max_salary: int = 1000000, saved_skill_filters_desc: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_error(x_token)
    filters = (min_salary, max_salary, saved_skill_filters_desc, salary_threshold_pct, allowed_missing_skills)
    return search_service.get_company_offers(*filters, user.id)

# --view professional offer (hide hidden)
@search_router.get('/professional_offer/{id}', tags=["Search Global"])
def view_approved_professional_offer(id: int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_professional_offer_by_id(id)

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
@search_router.get('/professional_offers', tags=["Search Global"])
def view_approved_professional_offers(min_salary: int = 0, max_salary: int = 1000000, saved_skill_filters_desc: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_error(x_token)
    filters = (min_salary, max_salary, saved_skill_filters_desc, salary_threshold_pct, allowed_missing_skills)
    return search_service.get_professional_offers(*filters, user.id)

@search_router.put('/propose_skills', tags=["Search Global"])
def propose_skills(skills: list = Body(default=["Skill1", "Skill2"]), x_token: str = Header()):
    user = user_or_error(x_token)
    if not skills:
        return Response(status_code=400)    
    skills = {s.capitalize():user.username for s in skills}
    return search_service.propose_new_skills(skills)


@search_router.post('/filter', tags=["Search Global"])
def save_filter(skill_filters:dict = Body(default={"Computers" : 1, "English": 1}), x_token: str = Header()):
    user = user_or_error(x_token)
    print(skill_filters)
    return search_service.add_webfilter(user.user_id, skill_filters)


@search_router.get('/filter', tags=["Search Global"])
def get_filters(x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_webfilters(user.user_id)








##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
# ####Professional:
@search_professional_router.get('/info', tags=["Professional"])
def view_approved_professional_self_info(x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_professional_by_id(user.id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/offer', tags=["Professional"])
def view_approved_hidden_professional_self_offer(id: int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_professional_offer_by_id(id, user.id, active=False) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/offers', tags=["Professional"])
def view_approved_hidden_professional_self_offers(min_salary: int = 0, max_salary: int = 1000000, saved_skill_filters_desc: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_error(x_token)
    filters = (min_salary, max_salary, saved_skill_filters_desc, salary_threshold_pct, allowed_missing_skills)
    return search_service.get_professional_offers(user.id, *filters, user.user_id, active=False) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/company_offer', tags=["Professional"])
def view_approved_active_company_offer(id:int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_company_offer_by_id(id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/company_offers', tags=["Professional"])
def view_approved_active_company_offers(min_salary: int = 0, max_salary: int = 1000000, saved_skill_filters_desc: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_error(x_token)
    filters = (min_salary, max_salary, saved_skill_filters_desc, salary_threshold_pct, allowed_missing_skills)
    return search_service.get_company_offers(*filters, user.id) if user.__class__.__name__ == 'Professional' else None

##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
# ####Company:
@search_company_router.get('/info', tags=["Companies"])
def view_approved_company_self_info(x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_company_by_id(user.id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/offer', tags=["Companies"])
def view_approved_archived_company_self_offer(id:int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_company_offer_by_id(id, user.id, active=False) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/offers', tags=["Companies"])
def view_approved_archived_company_self_offers(min_salary: int = 0, max_salary: int = 1000000, saved_skill_filters_desc: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_error(x_token)
    filters = (min_salary, max_salary, saved_skill_filters_desc, salary_threshold_pct, allowed_missing_skills)
    return search_service.get_company_offers(user.id, *filters, user.user_id, active=False) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/professional_offer', tags=["Companies"])
def view_approved_active_company_professional_offer(id:int,x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.get_professional_offer_by_id(id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/professional_offers', tags=["Companies"])
def view_approved_active_company_professional_offers(min_salary: int = 0, max_salary: int = 1000000, saved_skill_filters_desc: int | None = None, salary_threshold_pct: float = 20, allowed_missing_skills: int = 0, x_token: str = Header()):
    user = user_or_error(x_token)
    filters = (min_salary, max_salary, saved_skill_filters_desc, salary_threshold_pct, allowed_missing_skills, user.id)
    return search_service.get_professional_offers(*filters, user.id) if user.__class__.__name__ == 'Company' else None


###ADMIN:
##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
@search_admin_router.get('/company/{id}', tags=["Admin"])
def view_unapproved_company(id: int, x_token: str = Header()):
    admin = admin_or_error(x_token)
    return search_service.get_company_by_id(id, approved=False) if admin.__class__.__name__ == 'Admin' else None

@search_admin_router.get('/companies', tags=["Admin"])
def view_unapproved_companies(x_token: str = Header()):
    admin = admin_or_error(x_token)
    return search_service.get_companies(approved=False) if admin.__class__.__name__ == 'Admin' else None

@search_admin_router.get('/professional/{id}', tags=["Admin"])
def view_unapproved_professional(id: int, x_token: str = Header()):
    admin = admin_or_error(x_token)
    return search_service.get_professional_by_id(id, approved=False) if admin.__class__.__name__ == 'Admin' else None

@search_admin_router.get('/professionals', tags=["Admin"])
def view_unapproved_professionals(x_token: str = Header()):
    admin = admin_or_error(x_token)
    return search_service.get_professionals(approved=False) if admin.__class__.__name__ == 'Admin' else None
