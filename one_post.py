import telegram.error
from telegram import Bot
from dotenv import load_dotenv
import os
from pathlib import Path
from random import choice
import argparse


def send_image(image, bot, chat_id):
    try:
        with open(f'descriptions/{image}.txt', 'r') as file:
            description = file.read()
    except FileNotFoundError:
        description = None

    try:
        with open(f'images/{image}', 'rb') as file:
            if Path(image).suffix == '.gif':
                bot.send_animation(chat_id=chat_id, animation=file, caption=description)
            else:
                bot.send_photo(chat_id=chat_id, photo=file, caption=description)
    except telegram.error.BadRequest:
        with open(f'images/{image}', 'rb') as file:
            if Path(image).suffix == '.gif':
                post = bot.send_animation(chat_id=chat_id, animation=file)
            else:
                post = bot.send_photo(chat_id=chat_id, photo=file)
            bot.send_message(chat_id=chat_id, text=description, reply_to_message_id=post.message_id)


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
    image = args.image

    if not image:
        image = choice([image for image in os.listdir('images')])

    if not os.path.exists(f'images/{image}'):
        print(f'File "{image}" not found.')
        exit()

    bot = Bot(token=token)
    send_image(image, bot, chat_id)
