#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

    s1 = Square(10, 7, 2, 8)
    dictionary1 = s1.to_dictionary()
    json_dictionary1 = Base.to_json_string([dictionary1])
    print(dictionary1)
    print(type(dictionary1))
    print(json_dictionary1)
    print(type(json_dictionary1)) 
