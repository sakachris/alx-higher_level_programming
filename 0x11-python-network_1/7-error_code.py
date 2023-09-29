#!/usr/bin/python3
"""
module that takes in a URL, sends a request to the URL and
displays the body of the response
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    content = get(argv[1])
    if content.status_code >= 400:
        print("Error code:", content.status_code)
    else:
        print(content.text)
