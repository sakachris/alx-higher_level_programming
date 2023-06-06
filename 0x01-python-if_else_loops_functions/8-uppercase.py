#!/usr/bin/python3
def uppercase(str):
    converted = ''
    for c in str:
        v = ord(c)
        if (v >= 97 and v <= 122):
            converted += chr(v - 32)
        else:
            converted += c
    print("{}".format(converted))
