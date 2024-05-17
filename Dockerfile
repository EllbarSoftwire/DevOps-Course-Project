FROM python:3.10.14-alpine3.19 AS base

RUN pip install poetry
COPY pyproject.toml poetry.toml /todo_app/
WORKDIR /todo_app
RUN poetry install
COPY . .


FROM base as prod 
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host=0.0.0.0
EXPOSE 5000

FROM base AS dev
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host=0.0.0.0
EXPOSE 5000