from telegram import Bot
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text='Sample text')
