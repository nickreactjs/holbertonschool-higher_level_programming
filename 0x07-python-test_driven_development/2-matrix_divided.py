#!/usr/bin/python3
""" Module to divide all elements of a matrix"""


import math


def matrix_divided(matrix, div):
    check = 0
    check2 = 0
    if not isinstance(matrix, list):
        check = 1
    for i in matrix:
        if not isinstance(i, list):
            check = 1
            break
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                check = 1
                break
        lenr = len(matrix[0])
        if len(i) != lenr:
            check2 = 1
    if check == 1:
        raise TypeError('matrix must be a matrix (list of lists)\
        of integers/floats')
    if check2 == 1:
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(j / div, 2) for j in i] for i in matrix]


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
