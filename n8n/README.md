# Local n8n Setup

This folder contains a minimal `docker-compose` configuration for running n8n locally.

## Usage

1. Copy `.env.example` to `.env` and adjust the values if needed.
2. Start n8n:

```bash
docker-compose up -d
```

The n8n editor will be available at [http://localhost:5678](http://localhost:5678).

## Sample Workflow

The `workflows/telegram-recent-messages.json` file demonstrates how to fetch the
10 most recent updates from your Telegram bot. Import it through the n8n editor
or place it in the `data/workflows` folder before starting n8n.
