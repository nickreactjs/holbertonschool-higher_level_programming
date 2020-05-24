#!/usr/bin/python3
""" Say my name Module"""


def say_my_name(first_name, last_name=""):
    """Method for printing first and name.

    Args:
        first_name: string 1.
        last_name: string 2.

    Raises:
        TypeError: If one argument is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
