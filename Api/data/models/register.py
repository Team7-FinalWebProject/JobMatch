from pydantic import BaseModel, StringConstraints, field_validator
from typing import Annotated, Optional

Allowed_Username = Annotated[str, StringConstraints(pattern=r'^\w{2,20}$')]

class RegisterUserData(BaseModel):
    username: Allowed_Username
    approved: bool
    password: Optional[Annotated[str, StringConstraints(min_length=8, max_length=30)]] = None

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



