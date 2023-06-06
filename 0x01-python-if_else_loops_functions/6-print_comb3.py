#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(10):
        if digit1 != digit2 and digit1 < digit2:
            if digit1 <= 7 and digit2 <= 9:
                print("{}{}, ".format(digit1, digit2), end="")
            else:
                print("{}{}".format(digit1, digit2))
