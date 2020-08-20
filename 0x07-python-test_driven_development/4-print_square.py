#!/usr/bin/python3
""" Square Module"""


def print_square(size):
    """ print square
    Args:
    size: int
    returns: none
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        row = ''
        row = '#'* size
        row = row + '\n'
        print(row * size)
    else:
        print()

    if __name__ == '__main__':
        import doctest
        doctest.testfile("tests/4-print_square.txt")
