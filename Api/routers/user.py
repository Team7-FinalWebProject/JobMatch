from fastapi import APIRouter, Header, UploadFile, File
from fastapi.responses import FileResponse
from common.auth import professional_or_401
from common.auth import user_or_error, admin_or_error
from data.responses import BadRequest, Unauthorized, NotFound, Forbidden
from data.models.professional import ProfessionalInfoEdit
from data.models.offer import ProfessionalOfferCreate, ProfessionalOfferEdit
from services import professionals_service, login_service
from services.companies_service import check_offer_exists
from common.utils.file_uploader import create_upload_file
from common.utils.emailing import data_input, mailjet
import os
from pathlib import Path

users_router = APIRouter(prefix='/user')
_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED | NOT APPROVED]'


@users_router.get('/user_info', tags=['User'])
def get_user_info(x_token: str = Header()):
    user = user_or_error(x_token)
    return login_service.find_user_by_username(user.id) if user.__class__.__name__ == 'Professional' else None
