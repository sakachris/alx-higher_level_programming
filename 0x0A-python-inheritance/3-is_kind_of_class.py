#!/usr/bin/python3
"""
module for a function that tests for an instance
"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instance of the specified class
    """
    return isinstance(obj, a_class)
