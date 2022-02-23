from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    created: Optional[datetime]
    modified: Optional[datetime]
    name: str
    email: str
    gender: str
    birth_data: date
    telephone: str

    class Config:
        orm_mode = True


class UserSimple(BaseModel):
    name: str
    email: str
    gender: str
    birth_data: date
    telephone: str

    class Config:
        orm_mode = True


class UserEdit(BaseModel):
    name: str
    telephone: str

    class Config:
        orm_mode = True
