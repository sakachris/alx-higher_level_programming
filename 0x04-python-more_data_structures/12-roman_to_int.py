#!/usr/bin/python3
roman = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500),
              ('M', 1000), ('IV', 6), ('IX', 9), ('XL', 40),
              ('XC', 90), ('CD', 400), ('CM', 900)])


def roman_list(str):
    lst = []
    i = 0
    while (i < len(str)):
        if str[i:i+2] in roman:
            lst += [str[i:i+2]]
            i += 2
        else:
            lst += [str[i]]
            i += 1
    return lst


def roman_to_int(roman_string):
    num = 0
    lsts = roman_list(roman_string)
    for r in lsts:
        num += roman.get(r, 0)
    return num
