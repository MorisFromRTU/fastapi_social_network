from pydantic import BaseModel
from datetime import datetime

class UserItem(BaseModel):
    id: int
    username: str
    name: str
    surname: str
    email: str
    age: int
    registered_at: datetime

class UserRegister(BaseModel):
    username: str
    name: str
    surname: str
    email: str
    password: str

