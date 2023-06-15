#!/usr/bin/python3
roman = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500),
              ('M', 1000), ('IV', 4), ('IX', 9), ('XL', 40),
              ('XC', 90), ('CD', 400), ('CM', 900)])


def roman_list(rom_str):
    lst = []
    i = 0
    while (i < len(rom_str)):
        if rom_str[i:i+2] in roman:
            lst += [rom_str[i:i+2]]
            i += 2
        else:
            lst += [rom_str[i]]
            i += 1
    return lst


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    num = 0
    lsts = roman_list(roman_string)
    for r in lsts:
        num += roman.get(r, 0)
    return num
