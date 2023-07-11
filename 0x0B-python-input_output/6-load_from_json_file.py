#!/usr/bin/python3
"""
module for JSON conversion
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename) as file:
        return json.load(file)
