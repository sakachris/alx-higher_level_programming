#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for i in range(len(lst)):
            if (i != (len(lst)-1)):
                print("{:d} ".format(lst[i]), end="")
            else:
                print("{:d}".format(lst[i]), end="")
        print()
