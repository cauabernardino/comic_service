#!/usr/bin/env python3

import os
import requests
import subprocess
from bs4 import BeautifulSoup


def scraper():
    source = requests.get('https://c.xkcd.com/random/comic/').text
    soup = BeautifulSoup(source, features="html.parser")
    div = soup.find('div', id="comic")

    comic_url = 'https:' + div.img['src']
    
    return comic_url


def get_comics(directory, comic_url):
    
    subprocess.run(['wget', '-P', directory, comic_url])

    return 0


def check_files(directory):

    # Initialization of dict to store values
    files = {}

    # Get files path and download time
    for file in os.listdir(directory):
        path = os.path.join(directory, file)

        if os.path.isfile(path):
            dl_time = os.path.getctime(path)
            files[path] =  dl_time

    # Let maximum 2 files, delete oldest one
    sorted_files = sorted(files.items(), key=lambda x: x[1], reverse=True)
    
    while len(sorted_files) >= 2:   
        file_to_remove = sorted_files[-1]
        os.remove(file_to_remove[0])
        sorted_files.remove(file_to_remove)

    return 0



if __name__ == "__main__":
    dir = os.path.join(os.environ['HOME'], 'comicvault')
    comic = scraper()

    check_files(dir)
    get_comics(dir, comic)
