from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_latest_launch
from fetch_nasa_epic import fetch_epic
from fetch_nasa_apods import fetch_random_apods

if __name__ == "__main__":
    load_dotenv()
    fetch_spacex_latest_launch()
    fetch_epic()
    fetch_random_apods()
