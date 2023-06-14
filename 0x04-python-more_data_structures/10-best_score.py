#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    k = max(a_dictionary, key=lambda i: a_dictionary[i])
    return k
