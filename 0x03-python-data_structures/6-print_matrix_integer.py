#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ti in matrix:
        for dti in ti:
            print("{:d}".format(dti), end='')
            if ti.index(dti) != len(ti):
                print(" ", end='')
        print()
