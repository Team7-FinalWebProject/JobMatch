from pydantic import BaseModel, field_validator
from common.constraints import Allowed_Username, Allowed_Register_Password


class RegisterProfessionalData(BaseModel):
    username: Allowed_Username
    password: Allowed_Register_Password | None = None
    first_name: str
    last_name: str
    address: str
    summary: str

    @field_validator('password', mode='before')
    @classmethod
    def validate_password(cls, value: str):
        '''Iterates over password and checks
           if it contains all of the types of chars'''
        if value is None or value == '':
            return None
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
    password: Allowed_Register_Password | None = None
    company_name: str
    description: str
    address: str

    @field_validator('password', mode='before')
    @classmethod
    def validate_password(cls, value: str):
        '''Iterates over password and checks
           if it contains all of the types of chars'''
        if value is None or value == '':
            return None
        if (
            any(c.islower() for c in value) and
            any(c.isupper() for c in value) and
            any(c.isdigit() for c in value) and
            any(c in "@$!%*?&" for c in value)
        ):
            return value
        raise ValueError(
            "Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character (@$!%*?&).")