#!/usr/bin/python3
"""Square module"""


class Square:
    """square class

    Attributes:
        size

        """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """getter and setter size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate area"""
        return self.__size ** 2

    def my_print(self):
        """Print square to stdout with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
