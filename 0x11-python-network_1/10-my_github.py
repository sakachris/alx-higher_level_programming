#!/usr/bin/python3
"""
module that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = get(url, auth=(argv[1], argv[2])).json()
    print(response.get('id'))
