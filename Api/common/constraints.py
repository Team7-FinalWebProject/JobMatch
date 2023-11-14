from typing import Annotated, Optional
from pydantic import StringConstraints

Allowed_Username = Annotated[str, StringConstraints(pattern=r'^\w{2,20}$')]
Allowed_Register_Password = Optional[Annotated[str, StringConstraints(min_length=8, max_length=30)]]
Allowed_Login_Password = [Annotated[str, StringConstraints(min_length=8, max_length=30)]]