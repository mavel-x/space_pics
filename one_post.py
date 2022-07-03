from telegram import Bot
from dotenv import load_dotenv
import os
from pathlib import Path
from random import choice
import argparse

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser(
        description='Post an image to Telegram channel.'
    )
    parser.add_argument(
        'image',
        nargs='?',
        help='Image from the images directory to post (default: random).'
    )
    args = parser.parse_args()

    images_dir = Path('images')
    if not args.image:
        image = choice([image for image in images_dir.iterdir()])
    else:
        image = images_dir.joinpath(args.image)

    if not os.path.exists(image):
        print(f'File "{image}" not found.')
        exit()

    bot = Bot(token=token)
    with open(image, 'rb') as file:
        if image.suffix == '.gif':
            bot.send_animation(chat_id=chat_id, animation=file)
        else:
            bot.send_photo(chat_id=chat_id, photo=file)
