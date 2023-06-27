#!/usr/bin/python3
""" Class Square """


class Square:
    """ Initializing Square
    Args:
        __size: Private size of square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Public method area to calculate area of square
        Returns: Square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ public method my_print
            that prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()
