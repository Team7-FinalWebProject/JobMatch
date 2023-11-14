from pydantic import BaseModel, field_validator
from common.constraints import Allowed_Username, Allowed_Register_Password

class RegisterUserData(BaseModel):
    username: Allowed_Username
    approved: bool
    password: Allowed_Register_Password = None

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



