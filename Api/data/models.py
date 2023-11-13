from pydantic import BaseModel


class Company(BaseModel):
    id: int
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
    id: int
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
    username: str
    password: str


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