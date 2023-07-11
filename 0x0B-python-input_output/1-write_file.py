#!/usr/bin/python3
"""
module for file input/output
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and
    returns the number of characters written
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
