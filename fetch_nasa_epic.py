import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import argparse
from file_operations import save_remote_image


def fetch_epic(api_key, date=None):
    url = f'https://api.nasa.gov/EPIC/api/natural/'
    if date:
        url += f'date/{date}'
    params = {
        'api_key': api_key,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(error)
        return
    images = response.json()
    for index, image in enumerate(images):
        if index % 4:
            continue
        date = datetime.fromisoformat(image['date']).strftime('%Y/%m/%d')
        image_id = image['image']
        image_url = (f'https://api.nasa.gov/EPIC/archive/natural/'
                     f'{date}/png/{image_id}.png')
        save_remote_image(image_url, f'epic{index // 4}.png', params)
    print('Images saved.')


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_KEY')
    parser = argparse.ArgumentParser(
        description=(
            "Fetch images from DSCOVR's Earth Polychromatic Imaging Camera.")
        )
    parser.add_argument(
        'date',
        nargs='?',
        help='Date of shots (default: latest). Format: YYYY-MM-DD.',
    )
    args = parser.parse_args()
    fetch_epic(api_key, args.date)
