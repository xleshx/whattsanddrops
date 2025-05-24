FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:/root/.local/bin:$PATH"
RUN uv sync

CMD ["python", "bot.py"]
