
import os
import asyncio
from telegram import Update, Bot
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT1_TOKEN = os.environ["BOT1_TOKEN"]
BOT2_TOKEN = os.environ["BOT2_TOKEN"]
OWNER_ID = int(os.environ["OWNER_ID"])

bot2 = Bot(BOT2_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Хай, пиши, що какнуть 😎")

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    await bot2.send_message(
        chat_id=OWNER_ID,
        text=f"Нове повідомлення від користувача ID {message.from_user.id}"
    )

    await message.copy(chat_id=OWNER_ID, bot=bot2)

def main():
    app = Application.builder().token(BOT1_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.ALL & ~filters.COMMAND,
            forward_message
        )
    )
    app.run_polling()

if __name__ == "__main__":
    main()
