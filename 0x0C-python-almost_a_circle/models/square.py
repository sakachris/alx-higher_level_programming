#!/usr/bin/python3
"""
models/square.py for Square class
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}"
                .format(__class__.__name__, self.id, self.x, self.y,
                        self.size))

    def update(self, *args, **kwargs):
        """ Updates Square class arguments """
        ar = ['id', 'size', 'x', 'y']
        if not args and kwargs is not None:
            for var, val in kwargs.items():
                if var in ar:
                    setattr(self, var, val)
        for var, val in zip(ar, args):
            setattr(self, var, val)

    def to_dictionary(self):
        """ returns dictionary of a class instance """
        keys = ['size', 'x', 'y', 'id']
        dt = self.__dict__
        del (dt['_Rectangle__height'])
        dct = dict(zip(keys, list(dt.values())))
        return dct
