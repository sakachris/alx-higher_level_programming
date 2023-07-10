#!/usr/bin/python3
"""
module to set attriute
"""


def add_attribute(ob, key, value):
    """
    checks and sets attribute to object
    """
    if not hasattr(ob, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(ob, key, value)
