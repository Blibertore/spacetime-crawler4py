import os
from bs4 import BeautifulSoup


def get_url_files_dir():
    try:
        current_dir = str(os.getcwd())  # gets current working directory (path to scraper.py)
        start_index = current_dir.find(r"/fileProcessor.py")  # finds index within path of "/fileProcessor.py" begins
        if start_index != -1:
            # remove "/fileProcessor.py" from end of cwd & concatenate new directory
            url_files_directory = current_dir[0:start_index] + "/UrlFiles"
    except FileExistsError:
        pass

    return url_files_directory


def unique_pages():
    url_files_directory = get_url_files_dir()
    return len(os.listdir(url_files_directory))


def longest_page():
    url_files_directory = get_url_files_dir()
    for filename in os.listdir(url_files_directory):
        f = open(filename, "r")

