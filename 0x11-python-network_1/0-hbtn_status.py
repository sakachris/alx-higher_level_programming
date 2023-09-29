#!/usr/bin/python3
"""
module that fetches status
"""
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    utf = content.decode('utf-8')
    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {utf}")
