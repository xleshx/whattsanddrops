FROM python:3.13-slim-bookworm

# Copy uv from the official image
COPY --from=ghcr.io/astral-sh/uv:0.7.8 /uv /uvx /bin/

ADD . /app
WORKDIR /app

# Set environment variable for Python to not create .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Set environment variable to ensure output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1

# Sync the project into a new environment, asserting the lockfile is up to date
RUN uv sync --locked

CMD ["uv", "run", "whattsanddrops/main.py"]