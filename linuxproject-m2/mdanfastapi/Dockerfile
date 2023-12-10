# Dockerfile for mdanfastapi

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

RUN pip freeze > /app/requirements.txt

RUN pip install psycopg2-binary

RUN pip install databases

RUN pip install fastapi uvicorn

RUN pip install asyncpg

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install sqlalchemy

# Start de FastAPI-app wanneer de container wordt gestart
CMD ["uvicorn", "main:app"]


