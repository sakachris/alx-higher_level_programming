#!/usr/bin/python3
"""
Module containing LockedClass that prevents creation of new attributes
"""


class LockedClass:
    """
    Prevents addition of attributes
    """
    __slots__ = ["first_name"]
