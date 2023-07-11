#!/usr/bin/python3
"""
module for file input/output
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end="")
