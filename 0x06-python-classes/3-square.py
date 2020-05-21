#!/usr/bin/python3
"""Square class."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """init instance
            Args:
                size: length of side

            Raises:
                TypeError: size not int
                ValueError: size less than 0
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Area of square.

        Returns:
            squared size
        """
        return self.__size ** 2
