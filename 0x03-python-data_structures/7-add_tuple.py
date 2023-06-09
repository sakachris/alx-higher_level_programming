#!/usr/bin/python3
def two_elms(tupl=()):
    if (len(tupl) == 1):
        tupl += (0,)
        return tupl
    elif (len(tupl) == 0):
        tupl += (0, 0)
        return tupl
    else:
        return tupl


def add_tuple(tuple_a=(), tuple_b=()):
    a = two_elms(tuple_a)
    b = two_elms(tuple_b)
    return (a[0]+b[0], a[1]+b[1])
