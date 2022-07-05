import requests
import argparse
from file_operations import save_remote_image


def fetch_spacex_latest_launch():
    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(url)
    response.raise_for_status()
    launches = response.json()
    search_index = -1
    img_links = launches[search_index]['links']['flickr']['original']
    while not img_links:
        search_index -= 1
        img_links = launches[search_index]['links']['flickr']['original']
    for index, link in enumerate(img_links):
        save_remote_image(link, f'spacex_{index}.jpg')


def fetch_spacex_launch_by_id(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()
    img_links = launch['links']['flickr']['original']
    if not img_links:
        print('Sorry, no images for this launch.')
        return
    for index, link in enumerate(img_links):
        save_remote_image(link, f'spacex_{launch_id}_{index}.jpg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch SpaceX launch images by launch id.')
    parser.add_argument(
        'launch_id',
        nargs='?',
        help='Launch id (default: latest)',
    )
    args = parser.parse_args()
    print('Getting images from SpaceX...')
    if args.launch_id:
        fetch_spacex_launch_by_id(args.launch_id)
    else:
        fetch_spacex_latest_launch()
    print('Images saved.')
