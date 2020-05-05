#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for ti in matrix:
        i = 0
        if isinstance(ti, list):
            for dti in ti:
                i += 1
                print("{:d}".format(dti), end='')
                if i != len(ti):
                    print(" ", end='')
            i = 0
            print()
        else:
            print(ti)
