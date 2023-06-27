#!/usr/bin/python3
""" Class Square """


class Square:
    """ Initializing Square
    Args:
        __size: Private size of square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Public method area to calculate area of square
        Returns: Square area
        """
        return (self.__size * self.__size)
