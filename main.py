# coding: utf-8
"""
Description:
    This is a simple script for downloading GitHub specific directory instead clone whole repository

Date: 2022-02-17
Author: Clay Atlas
Website: https://clay-atlas.com
"""
from concurrent.futures import process
import html.parser
import re
import ssl
import urllib.request


def main():
    # Not to authenticate SSL certificate
    ssl._create_default_https_context = ssl._create_unverified_context

    # HtmlParser
    parser = html.parser.HTMLParser()

    # TODO: Need to change to customize
    github_url = "https://github.com"
    url = "https://github.com/ccs96307/LeetCode/"

    # Get the content
    f = urllib.request.urlopen(url)
    content = f.read().decode("utf-8")

    # Get the queue
    file_pattern = re.compile("<span class=\"css\-truncate css\-truncate\-target d\-block width\-fit\"><a class=\"js\-navigation\-open Link\-\-primary\" title=\".*\" data\-pjax=\"#repo\-content\-pjax\-container\" href=\"(.*)\">.*</a></span>")
    process_queue = file_pattern.findall(content)

    # Clean the dirty data (color-fg-muted)
    for i in range(len(process_queue)):
        if "color-fg-muted" in process_queue[i]:
            process_queue[i] = "/".join(process_queue[i].split("/")[:-1])

    while process_queue:
        item = parser.unescape(process_queue[0])

        if "color-fg-muted" in item:
            item = "/".join(item.split("/")[:-1])

        if "tree" in item:
            print(github_url+item)
            temp_f = urllib.request.urlopen(github_url+item)
            temp_content = temp_f.read().decode("utf-8")
            process_queue += file_pattern.findall(temp_content)

        elif "blob" in item:
            print(item, "is a file.")
        else:
            print(item, "is not a file...")
        
        process_queue = process_queue[1:]


if __name__ == "__main__":
    main()

