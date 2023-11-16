from pydantic import BaseModel, field_validator
from common.constraints import Allowed_Username, Allowed_Register_Password


class RegisterProfessionalData(BaseModel):
    username: Allowed_Username
    password: Allowed_Register_Password = None
    admin: str | None = None
    first_name: str
    last_name: str
    address: str
    user_id: str | None = None
    summary: str
    default_offer_id: int | None = None
    picture: bytes | None = None
    approved: bool | None = None

    @field_validator('password', mode='before')
    @classmethod
    def validate_password(cls, value):
        '''Iterates over password and checks
           if it contains all of the types of chars'''
        if (
            any(c.islower() for c in value) and
            any(c.isupper() for c in value) and
            any(c.isdigit() for c in value) and
            any(c in "@$!%*?&" for c in value)
        ):
            return value
        raise ValueError(
            "Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character (@$!%*?&).")
    

class RegisterCompanyData(BaseModel):
    username: Allowed_Username
    password: Allowed_Register_Password = None
    admin: bool | None = None
    company_name: str
    description: str
    address: str
    picture: bytes | None = None
    approved: bool | None = None
    user_id: int

    @field_validator('password', mode='before')
    @classmethod
    def validate_password(cls, value):
        '''Iterates over password and checks
           if it contains all of the types of chars'''
        if (
            any(c.islower() for c in value) and
            any(c.isupper() for c in value) and
            any(c.isdigit() for c in value) and
            any(c in "@$!%*?&" for c in value)
        ):
            return value
        raise ValueError(
            "Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character (@$!%*?&).")
    






#TODO see if better to be used out of the class

# def validate_password(cls, value):
#     '''Iterates over password and checks
#         if it contains all of the types of chars'''
#     if (
#         any(c.islower() for c in value) and
#         any(c.isupper() for c in value) and
#         any(c.isdigit() for c in value) and
#         any(c in "@$!%*?&" for c in value)
#     ):
#         return value
#     raise ValueError(
#         "Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character (@$!%*?&).")