from pydantic import BaseModel, Field
from typing import Any, Optional


class LoginForm(BaseModel):
    username:str = "username"
    password:str = "password"