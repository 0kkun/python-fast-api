from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from schemas.todo import Todo
from models.todo import TodoCreate, TodoList
from database import get_db

router = APIRouter()

@router.get("/todos", response_model=TodoList)
async def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return TodoList(todos=todos)

@router.post("/todos")
async def create_todos(todo_create: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo_create.title, content=todo_create.content, done=todo_create.done)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
