import os
from bs4 import BeautifulSoup


def get_url_files_dir():
    try:
        current_dir = str(os.getcwd())  # gets current working directory (path to scraper.py)
        url_files_directory = current_dir + "/UrlFiles"
        return url_files_directory
    except FileExistsError:
        pass


def unique_pages():
    url_files_directory = get_url_files_dir()
    return len(os.listdir(url_files_directory))


def longest_page():
    url_files_directory = get_url_files_dir()
    for filename in os.listdir(url_files_directory):
        f = open(filename, "r")

if __name__ == "__main__":
    print(get_url_files_dir())