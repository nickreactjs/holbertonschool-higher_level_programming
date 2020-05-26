#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Constructor.

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width.
        Raises:
            TypeError: If width != int
            ValueError: if width > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height
        Raises:
            TypeError: height != int
            ValueError: height < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
