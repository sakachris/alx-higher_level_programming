#!/usr/bin/python3
"""
module that fetches header id
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    response = get(argv[1])
    print(response.headers['X-Request-Id'])
