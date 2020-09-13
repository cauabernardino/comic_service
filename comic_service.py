#!/usr/bin/env python3

import os
import requests
import subprocess
from bs4 import BeautifulSoup


def main():
    # Define directory
    dir = os.path.join(os.environ['HOME'], 'comicvault') 
    
    # New comic url to download
    comic = scraper(dir)
    
    # Checking and downloading
    check_dir(dir)
    get_comics(dir, comic)

    return 0


def scraper(directory):
    """
    Gets an url for a comic that was not downloaded recently.
    """
    # Get new comic url
    source = requests.get('https://c.xkcd.com/random/comic/').text
    soup = BeautifulSoup(source, features="html.parser")
    div = soup.find('div', id="comic")
    
    # Checks if it's a new one, then returns url
    check_comic = div.img['src'].split('/')
    
    if check_comic[-1] not in os.listdir(directory):
        comic_url = 'https:' + div.img['src']
       
        return comic_url
    else:
        scraper(directory)
      

def get_comics(directory, comic_url):
    """
    Downloads comic to the given directory.
    """
    subprocess.run(['wget', '-P', directory, comic_url])

    return 0


def check_dir(directory, qty=2):
    """
    Checks for the chosen quantity of files in the given directory.
    The 'qty' parameters is the maximum amount of files to keep in the local filesystem.
    """
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
    
    while len(sorted_files) >= qty:   
        file_to_remove = sorted_files[-1]
        os.remove(file_to_remove[0])
        sorted_files.remove(file_to_remove)

    return 0
    

if __name__ == "__main__":
    main()
