from pydantic import BaseModel, StringConstraints, field_validator
from typing import Annotated, Optional


Allowed_Username = Annotated[str, StringConstraints(pattern=r'^\w{2,20}$')]


class Company(BaseModel):
    id: int | None = None
    username: str
    company_name: str
    password: str

    @classmethod
    def from_query_result(cls, id, username, company_name, password):
        return cls(
            id=id,
            username=username,
            company_name=company_name,
            password=password)


class Professional(BaseModel):
    id: int | None = None
    username: str
    first_name: str
    last_name: str
    password: str

    @classmethod
    def from_query_result(cls, id, username, first_name, last_name, password):
        return cls(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password)
    

class LoginData(BaseModel):
    username: Allowed_Username
    password: [Annotated[str, StringConstraints(min_length=8, max_length=30)]]


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


class User(BaseModel):
    id: int | None = None
    username: str
    approved: bool

    @classmethod
    def from_query_result(cls, id, username, approved):
        return cls(
            id=id,
            username=username,
            approved=approved)


class Message(BaseModel):
    id: int | None = None
    sender_username: str
    receiver_username: str
    content: str

    @classmethod
    def from_query_result(cls, id, sender_username, receiver_username, content):
        return cls(
            id=id,
            sender_username=sender_username,
            receiver_username=receiver_username,
            content=content)