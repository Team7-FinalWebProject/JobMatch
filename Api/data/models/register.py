from pydantic import BaseModel, field_validator
from common.constraints import Allowed_Username, Allowed_Register_Password


class RegisterUserData(BaseModel):
    username: Allowed_Username
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
    

class CompanyRegisterData(BaseModel):
    id: int | None = None
    name: str
    description: str
    address: str
    picture: bytes | None = None
    approved: bool

    # @classmethod
    # def from_query_result(cls, id, name, description, address, picture, approved):
    #     return cls(
    #         id=id,
    #         name=name,
    #         description=description,
    #         address=address,
    #         picture=picture,
    #         approved=approved)


