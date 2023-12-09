# main.py
from importlib import metadata
import databases
import sqlalchemy
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import socket
import os

DATABASE_URL = "postgresql://postgres:password@localhost/mydatabase"

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
# metadata.create_all(engine)
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_data(request: Request):
    # Example query
    query = "SELECT * FROM studentname;"
    with engine.connect() as connection:
        result = connection.execute(text(query))
        data = [dict(row) for row in result]

    return {
        "request": request,
        "data": data,
    }


class User(BaseModel):
    name: str

@app.get("/user")
async def read_user():
    return {"name": "Myrthe"}

@app.get("/container_id")
async def read_container_id():
    return {"container_id": socket.gethostname()}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


