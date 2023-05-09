from database import Base
from sqlalchemy import Column, String, Integer
from .mixins import TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"
    __table_args__ = {"comment": "USERテーブル"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, comment="ユーザー名")
    email = Column(String(50), unique=True, index=True, comment="メールアドレス")