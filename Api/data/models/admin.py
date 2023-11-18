from pydantic import BaseModel
from datetime import datetime

class Admin(BaseModel):
    id: int | None = None
    username: str | None = None
    issued: datetime | None = None

    @classmethod
    def from_query_result(cls, id, username, issued=None):
        return cls(
            id=id,
            username=username)