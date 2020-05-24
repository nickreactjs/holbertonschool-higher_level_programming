#!/usr/bin/python3
"""Integer addition module"""


def add_integer(a, b=98):
    """Add Integer

    Args:
        a: first int
        b: second int

    Raises:
        TypeError: if a, b are not int or float.

    Returns:
        Sum of both integers.
    """

    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
