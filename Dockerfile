FROM python:3.10.14-alpine3.19 AS base

RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.toml ./
RUN poetry install
COPY ./todo_app/ ./todo_app/

FROM base as prod 
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host=0.0.0.0
EXPOSE 5000

FROM base AS dev
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host=0.0.0.0
EXPOSE 5000

FROM base as test
COPY ./.env.test ./todo_app/
ENTRYPOINT poetry run pytest