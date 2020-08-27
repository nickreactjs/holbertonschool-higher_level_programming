#!/usr/bin/python3
""" Module for Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class. """

    def __init__(self, size):
        """ Init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return area."""
        return self.__size ** 2

    def __str__(self):
        """ str and print()"""
        return "[Square] {}/{}".format(self.__size, self.__size)
