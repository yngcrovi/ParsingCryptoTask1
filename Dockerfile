FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app


COPY ./poetry/pyproject.toml ./pyproject.toml
COPY ./poetry/poetry.lock ./poetry.lock
COPY ./src ./src

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry install --no-root
RUN poetry update

COPY . .