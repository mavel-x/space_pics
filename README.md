# space_pics
Fetch images from NASA and SpaceX and save them on disk.

## How to Install

### Get an API key from NASA
You will need an API key from [NASA Open APIs](https://api.nasa.gov/) &mdash; all you need is an email.

Create a file named ".env" in the project directory on your disk. This is where your API token
will be (more or less safely) stored. Add the following line to the file:
"NASA_KEY=_your_token_" (remove the quotation marks). The file will look like this:
```
NASA_KEY=9zTW8g51XWHSAqAJp9LrOnHzqT4wGoy1vWUuNCeT
```

### Install the Required Packages
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```console
$ pip install -r requirements.txt
```
Optionally, you can use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) 
to install the packages inside a virtual environment and not on your entire system. 
In this case you will need to run the script from the virtual environment as well.

### Run the Script
Open the terminal and run:
```console
$ python3 path/to/the/script/main.py 
```

## Project Purpose

The code is written for educational purposes as part of 
an online course for web developers at [dvmn.org](https://dvmn.org/).

## References
- [NASA Open APIs Guide](https://dev.bitly.com/get_started.html)
- [SpaceX API Guide](https://github.com/r-spacex/SpaceX-API)
- [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)
- [dvmn.org](https://dvmn.org/)
