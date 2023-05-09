from pydantic import BaseModel
from typing import List
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class UserList(BaseModel):
    __root__: List[User]