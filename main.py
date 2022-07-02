import requests
from pathlib import Path
import os
from urllib.parse import urlsplit
from datetime import datetime
from dotenv import load_dotenv


def save_image(url, filename, params=None):
    file = f'images/{filename}'
    response = requests.get(url, params)
    response.raise_for_status()
    with open(file, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    path = urlsplit(url).path
    root, extension = os.path.splitext(path)
    return extension


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(url)
    response.raise_for_status()
    json = response.json()

    search_index = -1
    img_links = json[search_index]['links']['flickr']['original']
    while not img_links:
        search_index -= 1
        img_links = json[search_index]['links']['flickr']['original']

    for index, link in enumerate(img_links):
        save_image(link, f'spacex_{index}.jpg')


def fetch_nasa_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': 30,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    json = response.json()
    images = [apod['url'] for apod in json if apod['media_type'] == 'image']
    for index, image in enumerate(images):
        extension = get_file_extension(image)
        save_image(image, f'nasa_apod_{index}{extension}')


def fetch_epic(api_key):
    url = f'https://api.nasa.gov/EPIC/api/natural/'
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for index, image in enumerate(images[:5]):
        date = datetime.fromisoformat(image['date']).strftime('%Y/%m/%d')
        image_id = image['image']
        image_url = (f'https://api.nasa.gov/EPIC/archive/natural/'
                     f'{date}/png/{image_id}.png')
        save_image(image_url, f'epic{index}.png', params)


if __name__ == "__main__":
    load_dotenv()
    nasa_key = os.getenv('NASA_KEY')
    Path("images").mkdir(exist_ok=True)
    fetch_spacex_last_launch()
    fetch_nasa_apod(nasa_key)
    fetch_epic(nasa_key)
