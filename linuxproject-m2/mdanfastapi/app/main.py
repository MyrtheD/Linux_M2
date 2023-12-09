
from typing import List
from typing import Union
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, String
import socket

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/mydatabase"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Fullname(Base):
    __tablename__ = "studentname"
    name = Column(String, primary_key=True)
                            
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/user")
def read_name(db:Session = Depends(get_db)):
     users = db.query(Fullname).all()
     return users