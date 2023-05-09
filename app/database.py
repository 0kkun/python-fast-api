from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
from sqlalchemy.orm import sessionmaker, Session

DATABASE = "mysql://%s:%s@%s/%s?charset=utf8" % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)

engine = create_engine(DATABASE, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
