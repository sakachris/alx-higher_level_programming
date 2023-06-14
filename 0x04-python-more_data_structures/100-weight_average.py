#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = [a * b for a, b in my_list]
    den = [b for a, b in my_list]
    return sum(num)/sum(den)
