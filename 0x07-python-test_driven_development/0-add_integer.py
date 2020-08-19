#!/usr/bin/python3
"""Module for add integer method"""


def add_integer(a, b=98):
    """
    add two integers
    Args:
        a: int
        b: int
    Returns:
        sum of a and b
    """

    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        x = int(a)
    else:
        x = a
    if isinstance(b, float):
        y = int(b)
    else:
        y = b
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
