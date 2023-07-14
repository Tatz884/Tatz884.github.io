from typing import Optional

from pydantic import BaseModel, Field

from .task import Task

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    user_key: str = Field("default_user_key", example="default_user_key")
    pass

class User(UserBase):
    id: int
    is_active: bool
    tasks: list[Task] = []

    class Config:
        orm_mode = True