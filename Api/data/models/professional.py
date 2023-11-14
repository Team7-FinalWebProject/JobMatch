from pydantic import BaseModel

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