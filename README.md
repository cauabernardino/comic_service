# Comic Service 

Download a new [xkcd](https://xkcd.com/) comic every hour and keeps a chosen quantity of them in the local filesystem at a time. Default is set on 2 comics.

## Remarks ✔

- Made for Linux systems
- It requires that you have `wget` installed on your system
- Scraping is made with `beautifulsoup4`

## How to run ⚙

- Clone this repo with

```bash
$ git clone https://github.com/cauabernardino/comic_service
```

- Make `addservice.sh` executable and run it
```bash
$ chmod +x addservice.sh

$ ./addservice.sh
```
- It will automatically create the target directory, install requirements and setup the `comic_service.py` script into the crontable to run every full hour.

    -  If you want the service to run every minute, you can change the `cronjob` variable in `addservice.sh`, by commenting current one and un-commenting the other.

- The comics will be stored at `/comicvault` in your home directory

- To remove the service you can use `crontab -e` to edit your crontable OR use `crontab -r` to remove it completely