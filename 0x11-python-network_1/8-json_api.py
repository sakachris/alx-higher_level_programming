#!/usr/bin/python3
"""
module that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    content = post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        # url = "http://0.0.0.0:5000/search_user"
        to_json = content.json()
        # to_json = post(url, {'q': letter}).json()
        id = to_json.get('id')
        name = to_json.get('name')
        if id or name:
            print(f"[{id}] {name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
