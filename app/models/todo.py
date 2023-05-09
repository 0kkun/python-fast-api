from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class Todo(BaseModel):
    id: int
    title: str = Field(..., max_length=30, description='タイトル')
    content: str = Field(..., max_length=300, description='内容')
    done: bool = Field(None, description='完了したかどうか')
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TodoCreate(BaseModel):
    title: str = Field(..., max_length=30, description='タイトル')
    content: str = Field(..., max_length=300, description='内容')
    done: bool = Field(None, description='完了したかどうか')

class TodoList(BaseModel):
    todos: List[Todo]