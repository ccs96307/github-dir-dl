# coding: utf-8
import os
import re
import requests


# Check the link is directory or not
def is_dir(url):
    if "tree" in url:
        return "tree"
    elif "blob" in url:
        return "blob"
    else:
        return "root"


def get_blob(url, save_location):
    None


def get_tree(url, save_location):
    None


def get_source(url, save_location):
    None


def list_tree():
    text = open("pic.html", "r").read()
    matches = re.findall("href=\"(/.+/.+/.+/.+/.+/.+)\">.+</a></span>", text)
    for match in matches: print(match)





def main():
    # Settings
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = "https://github.com/ccs96307/font-to-png/"
    raw_url = "https://github.com"

    # Crawl
    r = requests.get(url, headers=headers)

    # Find
    file_names = re.findall("href=\"(/.+/.+/\w+/\w+/.+)\">.+</a></span>", r.text)
    for file_name in file_names:
        url = raw_url + file_name
        
        if is_dir(url):
            r = requests.get(url, headers=headers)
            open("pic.html", "w").write(r.text)


if __name__ == "__main__":
    test()

