#!/usr/bin/python3
"""
Module for a Rectangle class
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        rect_str = ""
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for h in range(self.height):
            for w in range(self.width):
                rect_str += "#"
            if h < (self.height - 1):
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        return f"{__class__.__name__}({self.width}, {self.height})"
