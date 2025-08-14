import logging
from telegram import Update
from telegram.ext import Application, CommandHandler
from twilio.rest import Client
import config

# Twilio client
twilio_client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

async def start(update: Update, context):
    await update.message.reply_text("Send /call +380XXXXXXXXX to make a call")

async def call(update: Update, context):
    if not context.args:
        await update.message.reply_text("Usage: /call +380...")
        return

    phone = context.args[0]
    try:
        call = twilio_client.calls.create(
            to=phone,
            from_=config.TWILIO_PHONE_NUMBER,
            url="https://your-ngrok-url.ngrok.io/call?call_to=" + config.MY_CONTACT_URI
        )
        await update.message.reply_text(f"📞 Call initiated! SID: {call.sid}")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Логирование
logging.basicConfig(level=logging.INFO)

# Запуск бота
app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("call", call))

print("Bot is running...")
app.run_polling()
