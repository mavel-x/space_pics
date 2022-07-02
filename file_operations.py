import os
import requests
from pathlib import Path
from urllib.parse import urlsplit


def save_remote_image(url, filename, params=None):
    Path("images").mkdir(exist_ok=True)
    file = f'images/{filename}'
    response = requests.get(url, params)
    response.raise_for_status()
    with open(file, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    path = urlsplit(url).path
    root, extension = os.path.splitext(path)
    return extension
