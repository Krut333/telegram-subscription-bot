import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ВАШ_ТОКЕН_БОТА"
GROUP_LINK = "https://t.me/ВАША_ССЫЛКА_НА_ГРУППУ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здравствуйте! У вас есть доступ к группе в течение 30 дней.")

async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Ваша ссылка на группу: {GROUP_LINK}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("access", access))

    app.run_polling()
