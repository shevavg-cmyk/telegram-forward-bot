from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID"))

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        await update.channel_post.copy(chat_id=TARGET_CHAT_ID)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))

app.run_polling()
