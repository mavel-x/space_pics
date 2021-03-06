import os
import argparse
import requests
from dotenv import load_dotenv
from datetime import date, timedelta
from file_operations import get_file_extension_from_url, save_remote_image


def save_apods_with_descriptions(apods):
    for index, image in enumerate(apods, 1):
        url = image['url']
        extension = get_file_extension_from_url(url)
        img_filename = f'nasa_apod_random_{index}{extension}'
        description = (
            f'{image["title"]}\n'
            f'{image["explanation"]}\n'
        )
        save_remote_image(url, img_filename, description)


def fetch_random_apods(api_key, number_of_imgs=10):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': number_of_imgs,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apods = response.json()
    images = [apod for apod in apods if apod['media_type'] == 'image']
    save_apods_with_descriptions(images)


def fetch_latest_apods(api_key, number_of_days):
    start_date = date.today() - timedelta(days=number_of_days)
    formatted_start_date = start_date.strftime('%Y-%m-%d')

    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'start_date': formatted_start_date,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apods = response.json()
    images = [apod for apod in apods if apod['media_type'] == 'image']
    save_apods_with_descriptions(images)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Fetch a number of random NASA Astronomy Pictures of the Day. '
            'Note: if the APOD for a specific day was a video, it will be skipped, '
            'so you may occasionally get fewer images than requested.')
        )
    parser.add_argument(
        '-r', '--random',
        dest='n_random_images',
        metavar="N",
        nargs='?',
        const=10,
        type=int,
        help='Send N random images (default quantity: 10).',
    )
    parser.add_argument(
        '-l', '--latest',
        dest='n_latest_images',
        metavar="N",
        nargs='?',
        const=10,
        type=int,
        help='Send APODs for the last N days (default number of days: 10).',
    )
    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv('NASA_KEY')

    if args.n_random_images:
        fetch_random_apods(api_key, args.n_random_images)
    if args.n_latest_images:
        fetch_latest_apods(api_key, args.n_latest_images)
    if not args.n_random_images and not args.n_latest_images:
        fetch_random_apods(api_key)
    print('Images saved.')
