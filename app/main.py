from fastapi import FastAPI, Depends, HTTPException
from api import health_check, samples, items, tax
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List
from models.database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定
origins = [
    "http://localhost",
    "http://localhost:8080",
    # 他の許可するオリジンをここに追加する
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mysql+pymysql://<ユーザー名>:<パスワード>@<コンテナ名>:<ポート>/<データベース名>
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://python_fast_api_user:password@db:3366/python_fast_api_db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50), index=True)
#     email = Column(String(50), unique=True, index=True)

# Base.metadata.create_all(bind=engine)

class TodoCreate(BaseModel):
    title: str
    content: str

# class UserList(BaseModel):
#     __root__: List[User]

# @app.post("/todos")
# async def create_user(todo: TodoCreate, db: Session = Depends(get_db)):
#     db_todo = todo(title=todo.title, content=todo.content)
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo

# @app.get("/users/", response_model=UserList)
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = db.query(User).offset(skip).limit(limit).all()
#     return {"__root__": users}

# @app.get("/users/{user_id}")
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @app.put("/users/{user_id}")
# def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     db_user.name = user.name
#     db_user.email = user.email
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     db.delete(db_user)
#     db.commit()
#     return {"message": "User deleted"}

app.include_router(health_check.router, tags=["health_check"])
app.include_router(samples.router, tags=["sample"])
app.include_router(items.router, tags=["item"], responses={404: {"description": "Not found"}})
app.include_router(tax.router, tags=["tax"])