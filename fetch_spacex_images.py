import requests
import argparse
from datetime import date
from file_operations import save_remote_image


def fetch_spacex_latest_images():
    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(url)
    response.raise_for_status()
    launches = response.json()

    # Not all launches have images, so we search backwards starting at the latest one
    # until we find a launch that has some images.
    search_index = -1
    img_links = launches[search_index]['links']['flickr']['original']
    while not img_links:
        search_index -= 1
        img_links = launches[search_index]['links']['flickr']['original']
    launch_date = date.fromtimestamp(launches[search_index]['date_unix'])
    description = f'SpaceX launch {launch_date}.'
    for index, link in enumerate(img_links, 1):
        save_remote_image(link, f'spacex_{index}.jpg', description)


def fetch_spacex_launch_by_id(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()
    img_links = launch['links']['flickr']['original']
    assert img_links
    launch_date = date.fromtimestamp(launch['date_unix'])
    description = f'SpaceX launch {launch_date}.'
    for index, link in enumerate(img_links, 1):
        save_remote_image(link, f'spacex_{launch_id}_{index}.jpg', description)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch SpaceX launch images by launch id.')
    parser.add_argument(
        'launch_id',
        nargs='?',
        help='Launch id (default: latest)',
    )
    args = parser.parse_args()

    if args.launch_id:
        try:
            fetch_spacex_launch_by_id(args.launch_id)
            print('Images saved.')
        except AssertionError:
            print('Sorry, no images for this launch.')
    else:
        fetch_spacex_latest_images()
        print('Images saved.')
