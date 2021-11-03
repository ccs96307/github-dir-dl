# coding: utf-8
import re
import requests


# Check the link is directory or not
def is_dir(url):
    




def main():
    # Settings
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    user = "ytdl-org"
    project_name = "youtube-dl/tree/master/.github"
    url = "https://github.com/{}/{}/".format(user, project_name)
    raw_url = "https://raw.githubusercontent.com/{}/{}/".format(user, project_name)

    # Crawl
    r = requests.get(url, headers=headers)

    # Filter
    file_names = re.findall("href=\"/{}/{}/\w+/(\w+/.+)\">(.+)</a></span>".format(user, project_name), r.text)
    extension_pattern = ".py"

    print(file_names)

    for f in file_names:
        if f[1].endswith(extension_pattern):
            print("○ {}".format(f[1]))
            file_url = raw_url + f[0]
            print(file_url)
            exit()
            source_code = requests.get(file_url, headers=headers)
            
            # Save file
            open(f[1], "w").write(source_code.text)
        else:
            print("✕ {}".format(f[1]))


if __name__ == "__main__":
    main()

