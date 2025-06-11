from __future__ import annotations

import asyncio
import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

import database
from handlers import business, client


async def main() -> None:
    load_dotenv()
    await database.init_db()

    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise SystemExit("TELEGRAM_TOKEN not set")

    application = Application.builder().token(token).build()

    # Business handlers
    application.add_handler(business.setup())
    application.add_handler(CommandHandler("ai", business.ai_command))

    # Client handlers
    for handler in client.setup():
        application.add_handler(handler)

    await application.initialize()
    await application.start()
    print("Bot started")
    await application.updater.start_polling()
    await application.updater.idle()


if __name__ == "__main__":
    asyncio.run(main())
