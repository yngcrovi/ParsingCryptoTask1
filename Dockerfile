FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app


COPY ./poetry/pyproject.toml ./pyproject.toml
COPY ./src ./src

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev 

COPY . .