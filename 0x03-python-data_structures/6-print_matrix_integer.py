#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, v in enumerate(i):
            if j < len(i) - 1:
                print("{} ".format(v), end='')
            else:
                print("{}".format(v))
