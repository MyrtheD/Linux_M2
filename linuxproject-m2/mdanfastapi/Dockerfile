# Dockerfile for mdanfastapi

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

RUN pip freeze > /app/requirements.txt

RUN pip install psycopg2

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install sqlalchemy

# RUN uvicorn main:app --reload


