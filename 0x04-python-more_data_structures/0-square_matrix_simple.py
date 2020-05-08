#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    sm = []
    for idx in matrix:
        sm.append(list(map(lambda x: x**2, idx)))
    return (sm)
