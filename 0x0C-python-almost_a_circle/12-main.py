#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)
    r2_dictionary = r2.to_dictionary()
    print(r2_dictionary)

    r3 = Rectangle(50, 60)
    print(r3)
    r3_dictionary = r3.to_dictionary()
    print(r3_dictionary)
    print(type(r3_dictionary))
 
