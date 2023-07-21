#!/usr/bin/python3
"""
models/rectangle.py for Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ returns area of rectangle """
        return self.width * self.height

    def display(self):
        """ prints the rectangle to stdout """
        for m in range(self.y):
            print("")
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """ string output of instances """
        return ("[{}] ({}) {}/{} - {}/{}"
                .format(__class__.__name__, self.id, self.x, self.y,
                        self.width, self.height))

    def update(self, *args, **kwargs):
        """ Updates Rectangle class arguments """
        ar = ['id', 'width', 'height', 'x', 'y']
        if not args and kwargs is not None:
            for var, val in kwargs.items():
                if var in ar:
                    setattr(self, var, val)
        for var, val in zip(ar, args):
            setattr(self, var, val)

    def to_dictionary(self):
        """ returns dictionary of a class instance """
        keys = ['width', 'height', 'x', 'y', 'id']
        dct = dict(zip(keys, list(self.__dict__.values())))
        return dct
