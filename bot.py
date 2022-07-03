from telegram import Bot
from dotenv import load_dotenv
import os
from pathlib import Path
from file_operations import get_file_extension

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = Bot(token=token)
    images_dir = Path('images')
    images = [x for x in images_dir.iterdir()]
    image = images[0]
    with open(image, 'rb') as file:
        if image.suffix == '.gif':
            bot.send_animation(chat_id=chat_id, animation=file)
        else:
            bot.send_photo(chat_id=chat_id, photo=file)