import os
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_latest_images
from fetch_nasa_epic import fetch_epic
from fetch_nasa_apods import fetch_random_apods

if __name__ == "__main__":
    load_dotenv()
    nasa_key = os.getenv('NASA_KEY')

    print('Getting images from SpaceX...')
    fetch_spacex_latest_images()
    print('Getting images from NASA EPIC...')
    fetch_epic(nasa_key)
    print('Getting images from NASA APOD...')
    fetch_random_apods(nasa_key)
    print('Images saved.')
