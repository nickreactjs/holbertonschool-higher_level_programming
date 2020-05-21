#!/usr/bin/python3
"""Square Module."""


class Square:
    """Define a Square."""

    def __init__(self, size=0):
        """Init.

        Args:
            size(int): size of length

        Raises:
            TypeError: If size not integer.
            ValueError: If size less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area
            Return area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Property.

            Retreive size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter size
            change size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
