#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    pop_list = [i for i in a_dictionary if a_dictionary[i] == value]
    for n in pop_list:
        a_dictionary.pop(n, "")
    return a_dictionary
