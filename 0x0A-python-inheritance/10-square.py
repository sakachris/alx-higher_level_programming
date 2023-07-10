#!/usr/bin/python3
"""
module for Square class inheriting Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting Rectangle class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
