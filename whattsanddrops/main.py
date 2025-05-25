"""Main module for whattsanddrops."""

import os
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am your bot!")


def main() -> None:
    # Load environment variables from .env file if it exists
    env_path = Path('.env')
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN environment variable not set")

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == "__main__":
    main()
