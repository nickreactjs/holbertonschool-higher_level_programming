#!/usr/bin/python3
"""This module contains a Square class."""


class Square:
    """ This class defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Calculate square of size."""
        return self.__size ** 2

    def my_print(self):
        """ Print out the square."""
        if self.size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.size):
                print(' ' * self.__position[0], end='')
                for j in range(self.size):
                    print('#', end='')
                print()

    @property
    def size(self):
        """ Property and setter of size."""
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
        """ Property and setter for positon"""
        return self.position

    @position.setter
    def position(self, tuplep):
        if not isinstance(tuplep, tuple) or len(tuplep) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if tuplep[1] < 0 or tuplep[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = tuplep
