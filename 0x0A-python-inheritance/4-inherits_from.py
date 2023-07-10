#!/usr/bin/python3
"""
module for a function that tests for a subclass
"""


def inherits_from(obj, a_class):
    """
    checks if the object is a subclass of the specified class
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
