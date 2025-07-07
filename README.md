# Whattsanddrops

A simple Telegram bot project managed with uv.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

### Installation

```bash
# Install the project and its dependencies
uv pip install -e .

# For development dependencies
uv pip install -e ".[dev]"
```

## Usage

Set the `TELEGRAM_TOKEN` environment variable and run:

```bash
python -m whattsanddrops.main
```

## Deployment

The project includes a GitHub Actions workflow that builds a Docker image and pushes it to [GitHub Container Registry](https://ghcr.io). Authentication is handled automatically using `GITHUB_TOKEN`.

### Render

To deploy the bot on [Render](https://render.com), connect your repository and enable **Auto Deploy**. The included `render.yaml` file configures a Docker based worker service. Set the `TELEGRAM_TOKEN` environment variable in the Render dashboard and the bot will start automatically after each push to the `main` branch.

## Local n8n Setup

A minimal `docker-compose` configuration for running n8n locally is provided in the `n8n` directory:

```bash
cd n8n
cp .env.example .env
docker-compose up -d
```

This will start n8n at [http://localhost:5678](http://localhost:5678).

The `n8n/workflows` directory includes a sample workflow that fetches the ten
most recent messages from your Telegram bot using the Telegram API.
