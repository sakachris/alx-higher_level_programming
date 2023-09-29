#!/usr/bin/python3
"""
module that takes in a URL, sends a request to the URL and
displays the body of the response
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print("Error code:", e.code)
