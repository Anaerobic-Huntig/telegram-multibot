from __future__ import annotations

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from database import get_business_by_code, get_items_for_business
from ai_helper import ask_gpt

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if args and args[0].startswith("biz_"):
        code = args[0].split("biz_")[-1]
        biz = await get_business_by_code(code)
        if not biz:
            await update.message.reply_text("Business not found.")
            return
        items = await get_items_for_business(biz[0])
        message = [f"Welcome to {biz[2]}!"]
        for item in items:
            message.append(f"- {item[1]}: {item[2]} (${item[3]})")
        if not items:
            message.append("No items yet.")
        await update.message.reply_text("\n".join(message))
    else:
        await update.message.reply_text("Use a business link to see their catalog.")

async def advisor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Ask me anything about the products!")
        return
    reply = await ask_gpt(prompt)
    await update.message.reply_text(reply)


def setup() -> list[CommandHandler]:
    return [
        CommandHandler("start", start),
        CommandHandler("advisor", advisor),
    ]
