from telegram import Bot
from dotenv import load_dotenv
import os
from pathlib import Path
from random import shuffle
import time
import argparse

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    post_frequency = os.getenv('POST_FREQUENCY')
    if not post_frequency:
        post_frequency = 4

    parser = argparse.ArgumentParser(
        description='Post space images from images directory every N hours.'
    )
    parser.add_argument(
        'frequency',
        nargs='?',
        type=int,
        default=post_frequency,
        help='Number of hours between posts'
    )
    args = parser.parse_args()

    bot = Bot(token=token)
    images_dir = Path('images')
    images = [image for image in images_dir.iterdir()]

    while True:
        for image in images:
            with open(image, 'rb') as file:
                if image.suffix == '.gif':
                    bot.send_animation(chat_id=chat_id, animation=file)
                else:
                    bot.send_photo(chat_id=chat_id, photo=file)
            time.sleep(3600 * args.frequency)
        shuffle(images)
