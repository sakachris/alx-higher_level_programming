#!/usr/bin/python3
"""
module for class to JSON
"""


def class_to_json(obj):
    """
    returns dictionary description for JSON serialization
    """
    return vars(obj)
