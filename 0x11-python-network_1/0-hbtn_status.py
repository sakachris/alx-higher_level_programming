#!/usr/bin/python3
"""
module that fetches status
"""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        utf = content.decode('utf-8')
        print("Body response:")
        print(f"\t - type: {type(content)}")
        print(f"\t - content: {content}")
        print(f"\t - utf8 content: {utf}")
