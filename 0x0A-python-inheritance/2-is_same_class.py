#!/usr/bin/python3
"""
module for a function that tests for an instance
"""


def is_same_class(obj, a_class):
    """
    checks if the object is exactly an instance of the specified class
    """
    return type(obj) == a_class
