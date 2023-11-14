from pydantic import BaseModel, StringConstraints
from typing import Annotated

Allowed_Username = Annotated[str, StringConstraints(pattern=r'^\w{2,20}$')]

class LoginData(BaseModel):
    username: Allowed_Username
    password: [Annotated[str, StringConstraints(min_length=8, max_length=30)]]
