#!/usr/bin/python3
"""
module to search and update file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, encoding='UTF-8') as file:
        lines = file.readlines()

    with open(filename, "w", encoding='UTF-8') as file:
        for line in lines:
            if search_string in line:
                line += new_string
            file.write(line)
