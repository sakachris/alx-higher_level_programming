#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_keys = list(a_dictionary.keys())
    ord_keys.sort()
    for i in ord_keys:
        print("{}: {}".format(i, a_dictionary[i]))
