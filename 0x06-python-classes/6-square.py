#!/usr/bin/python3
"""Square module"""


class Square:
    """square class

    Attributes:
        size

        """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter and setter position."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area"""
        return self.__size ** 2

    def my_print(self):
        """Print square to stdout with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
