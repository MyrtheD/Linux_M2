from typing import List
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

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/user")
async def read_name(db:Session = Depends(get_db)):
     users = db.query(Fullname).all()
     return users

# @app.get("/user")
# async def read_user():
#    return {"name": "Myrthe"}

@app.get("/container_id")
async def read_container_id():
    return {"container_id": socket.gethostname()}


