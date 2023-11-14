from pydantic import BaseModel
from common.constraints import Allowed_Username, Allowed_Login_Password

class LoginData(BaseModel):
    username: Allowed_Username
    password: Allowed_Login_Password
