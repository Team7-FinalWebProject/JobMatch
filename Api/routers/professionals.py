from fastapi import APIRouter, Header
from common.auth import user_or_401
from data.responses import BadRequest, Unauthorized
from data.models.register import RegisterUserData
from data.models.professional import Professional
from data.models.company import Company
from services import register_service


professionals_router = APIRouter(prefix='/professionals')


@professionals_router.put('/info')
def edit_info(x_token: str = Header(default=None)):
    pass


@professionals_router.put('/offer')
def set_prof_offer(x_token: str = Header(default=None)):
    pass


@professionals_router.post('/offer')
def create_offer(x_token: str = Header(default=None)):
    pass


@professionals_router.put('/edit/offer')
def edit_prof_offer(x_token: str = Header(default=None)):
    pass


@professionals_router.post('/match')
def create_match_request(x_token: str = Header(default=None)):
    pass


@professionals_router.get('/requests')
def view_match_requests(x_token: str = Header(default=None)):
    pass


@professionals_router.put('/archive')
def archive_prof_offer(x_token: str = Header(default=None)):
    pass