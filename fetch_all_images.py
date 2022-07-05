import os
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_latest_images
from fetch_nasa_epic import fetch_epic
from fetch_nasa_apods import fetch_random_apods

if __name__ == "__main__":
    load_dotenv()
    nasa_key = os.getenv('NASA_KEY')

    fetch_spacex_latest_images()
    fetch_epic(nasa_key)
    fetch_random_apods(nasa_key)
