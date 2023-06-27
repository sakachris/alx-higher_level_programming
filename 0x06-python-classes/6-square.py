#!/usr/bin/python3
""" Class Square """


class Square:
    """ Initializing Square
    Args:
        __size: Private size of square
        __position: Private position of square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ Public method area to calculate area of square
        Returns: Square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ public method my_print
            that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for s in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end='')
                print()
