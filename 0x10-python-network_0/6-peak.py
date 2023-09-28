#!/usr/bin/python3
"""
module to find peak elements of an array
"""


def find_peak(list_of_integers):
    """
    finds peak elements of a list
    """
    if not list_of_integers:
        return

    beg = 0
    end = len(list_of_integers) - 1

    while beg < end:
        mid = (beg + end) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            beg = mid + 1
    return list_of_integers[beg]
