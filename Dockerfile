FROM python:3.13-slim-bookworm

WORKDIR /enroll
COPY . .

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
RUN uv sync --frozen --no-dev

CMD [ "uv", "run", "enroll.py" ]
