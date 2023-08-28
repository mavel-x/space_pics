# space_pics
Post images from NASA and SpaceX on your Telegram channel.

## How to Install

### Get an API key from NASA
You will need an API key from [NASA Open APIs](https://api.nasa.gov/) &mdash; all you need is an email.

Create a file named ".env" in the project directory on your disk. This is where your API token
will be (more or less safely) stored. Add the following line to the file:
"NASA_KEY=_your_token_" (remove the quotation marks). The file will look like this:
```
NASA_KEY=9zTW8g51XWHSAqAJp9LrOnHzqT4wGoy1vWUuNCeT
```

### Create a Telegram bot and get your API token
If you've never created a bot before, here is a 
[tutorial](https://github.com/python-telegram-bot/v13.x-wiki/wiki/Introduction-to-the-API) 
from the authors of python-telegram-bot.
Put the token into your .env file like this:
```
TG_TOKEN=1234567890:AAHfiqksKZ8WmR2zSjiQ7_v4TMAKdiHm9T0
```

### Create a Telegram chat
In Telegram app, press "Create channel" and follow the simple steps.
When you are done, get the chat id (as "@your_channel") and add it to the .env file:
```
TG_CHAT_ID=@your_channel
```

### Install the required packages
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```console
$ pip install -r requirements.txt
```
Optionally, you can use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) 
to install the packages inside a virtual environment and not on your entire system. 
In this case you will need to run the script from the virtual environment as well.

## How to Use

### Download space pics
Open the terminal and run:
```console
$ python3 path/to/the/script/fetch_all_images.py
```
A directory called "images" will be created in the project directory and filled with space pics.

Alternatively, you can download only pictures from a specific API with the scripts **fetch_nasa_apods.py**,
**fetch_nasa_epic.py**, and **fetch_spacex_images.py**. To find out how to use them, run the scripts with the argument `-h`.

### Post a single image on your Telegram channel
Run **one_post.py**, passing name of the image you would like send as an argument. 
Only files from the images directory inside the project directory are allowed.
```console
$ python3 one_post.py image.png
```
If no argument is passed, a random image is chosen.
```console
$ python3 one_post.py
```
### Post pictures on your Telegram channel while you sleep
The **auto_post.py** script will run in an infinite loop until interrupted (Ctrl+C). Start it from the terminal:
```console
$ python3 auto_post.py
```
\
By default, a post will be published every 4 hours. To change this, either add a parameter to 
the .env file like so:
```
POST_FREQUENCY=6
```
or pass the desired number of hours to the script when you run it:
```console
$ python3 path/to/the/script/bot.py 6
```

## References
- [NASA Open APIs Guide](https://dev.bitly.com/get_started.html)
- [SpaceX API Guide](https://github.com/r-spacex/SpaceX-API)
- [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)
