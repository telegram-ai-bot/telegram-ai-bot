import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("8589242222:AAF8rkxRfHyS-jcNBBtLh2wpWi_3_eKidpg")

async def start(update, context):
    await update.message.reply_text("AI Bot অনলাইন ✅")

async def reply(update, context):
    text = update.message.text.lower()

    if "hi" in text or "hello" in text:
        answer = "Hello! কেমন আছো?"
    elif "name" in text:
        answer = "আমার নাম Python AI Bot."
    else:
        answer = "আমি এখনো শিখছি 🤖"

    await update.message.reply_text(answer)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
