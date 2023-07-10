#!/usr/bin/python3
"""
module containing lookup function for listing attrubites & objects
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    return dir(obj)
