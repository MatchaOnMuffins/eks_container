FROM ghcr.io/astral-sh/uv:python3.12-alpine

ADD pyproject.toml /app/
ADD uv.lock /app/

WORKDIR /app
RUN uv sync --no-default-groups

ADD . /app


ENV PORT=8000
EXPOSE ${PORT}

CMD uv run uvicorn src.main:app --host 0.0.0.0 --port $PORT