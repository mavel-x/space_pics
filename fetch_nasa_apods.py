import os
import argparse
import requests
from dotenv import load_dotenv
from file_operations import save_remote_image, get_file_extension_from_url


def fetch_random_apods(api_key, number_of_imgs=10):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': number_of_imgs,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apods = response.json()
    image_links = [apod['url'] for apod in apods if apod['media_type'] == 'image']
    for index, link in enumerate(image_links, 1):
        extension = get_file_extension_from_url(link)
        save_remote_image(link, f'nasa_apod_{index}{extension}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Fetch a number of random NASA Astronomy Pictures of the Day. '
            'Note: if the APOD for a specific day was a video, it will be skipped, '
            'so you may occasionally get fewer images than requested.')
        )
    parser.add_argument(
        'number_of_imgs',
        nargs='?',
        default=10,
        type=int,
        help='Number of images (default: 10).',
    )
    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv('NASA_KEY')

    print('Getting images from NASA APOD...')
    fetch_random_apods(args.number_of_imgs)
    print('Images saved.')
