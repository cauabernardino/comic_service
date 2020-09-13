#!/usr/bin/env bash

echo "Creating target directory...";
mkdir $HOME/comicvault;

echo "Installing dependencies...";
python3 -m pip install -r ./requirements.txt;

echo "Making the script executable..."
chmod +x $PWD/comic_service.py;

echo "Appending (or creating) crontable...";
cronjob="0 * * * * $PWD/comic_service.py > /dev/null 2>&1";
crontab -l > tmpfile;
echo "$cronjob" >> tmpfile; 
crontab tmpfile;
rm tmpfile;

echo
echo "The current crontable is now:";
crontab -l;