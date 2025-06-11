from __future__ import annotations

import secrets

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters

from database import add_business
from ai_helper import ask_gpt

ASK_NAME, ASK_TYPE, ASK_CONTACT = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Enter your business name:")
    return ASK_NAME

async def ask_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["biz_name"] = update.message.text
    await update.message.reply_text("What do you offer? (products/services)")
    return ASK_TYPE

async def ask_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["biz_type"] = update.message.text
    await update.message.reply_text("Contact info (email or phone):")
    return ASK_CONTACT

async def finish_registration(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    contact = update.message.text
    name = context.user_data["biz_name"]
    biz_type = context.user_data["biz_type"]
    start_code = secrets.token_hex(3)
    await add_business(update.effective_user.id, name, biz_type, contact, start_code)
    link = f"/start biz_{start_code}"
    await update.message.reply_text(f"Registration complete! Share this link with your clients: {link}")
    return ConversationHandler.END

async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Usage: /ai <your question>")
        return
    reply = await ask_gpt(prompt)
    await update.message.reply_text(reply)


def setup() -> ConversationHandler:
    conv = ConversationHandler(
        entry_points=[CommandHandler("register", start)],
        states={
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_type)],
            ASK_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_contact)],
            ASK_CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, finish_registration)],
        },
        fallbacks=[],
    )
    return conv
