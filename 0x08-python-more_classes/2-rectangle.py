#!/usr/bin/python3
"""Module for Rectangle class number 2."""


class Rectangle:
    """Define a simple Rectangle."""

    def __init__(self, width=0, height=0):
        """Constructor.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property for the width of the rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Raises:
        TypeError: width != int
        ValueError: width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width myst be >=0")
        self.__width = value

    @property
    def height(self):
        """Property for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Raises:
            TypeError: width != int
            ValueError: width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width myst be >=0")
        self.__height = value

    def area(self):
        """Return are of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle."""
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2
