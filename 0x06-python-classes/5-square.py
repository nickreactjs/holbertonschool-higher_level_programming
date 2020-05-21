#!/usr/bin/python3
"""Square module."""


class Square:
    """Define Square"""

    def __init__(self, size=0):
        """Init

        Args:
            size: Length of side.
        """
        self.__size = size

    @property
    def size(self):
        """Property

        Raises:
            TypeError: size != int
            ValueError: size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area

        Returns:
            size squared
        """
        return self.__size ** 2

    def my_print(self):
        """Pritn square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='\n' if j is self.__size - 1 and i != j else '')
        print()
