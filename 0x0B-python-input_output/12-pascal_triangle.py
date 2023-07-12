#!/usr/bin/python3
"""
module for pascal triangle
"""


def pascal_triangle(n):
    """
    that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    lst = [[1]]
    for i in range(n-1):
        nlst = []
        for k in range(len(lst[i])+1):
            nlst.extend([([0]+lst[i]+[0])[k] + ([0]+lst[i]+[0])[k+1]])
        lst.append(nlst)
    return lst
