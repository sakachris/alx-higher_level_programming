#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    '''r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1])

    with open("Rectangle.json", "r") as file:
        print(file.read())'''

    Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])
