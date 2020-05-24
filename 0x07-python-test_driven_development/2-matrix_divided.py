#!/usr/bin/python3
"""Matrix_Divided Module"""


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix
    Args:
        matrix: List of lists containing float or int
        div: divident of matrix
    Returns:
        list: new matrix
    Raises:
        TypeError: If matrix contains diffenerent elemts than int or float
        TypeError: If sublists are inequivalent in size.
        TypeError: Div != int && float
        ZeroDivisionError: Div == 0
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for ti in matrix:
        if not isinstance(ti, list) or len(ti) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(ti) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in ti:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in ti] for ti in matrix]
