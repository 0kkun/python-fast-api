from database import Base
from sqlalchemy import Column, String, Integer, Boolean
from .mixins import TimestampMixin

class Todo(Base, TimestampMixin):
    __tablename__ = 'todos'
    __table_args__ = {"comment": "TODOテーブル"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False, comment="タイトル")
    content = Column(String(300), nullable=False, comment="内容")
    done = Column(Boolean, default=False, comment="完了したかどうか")