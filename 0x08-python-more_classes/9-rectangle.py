#!/usr/bin/python3
"""Module for Rectangle class number 2."""


class Rectangle:
    """Define a simple Rectangle."""

    number_of_instances = 0
    """int: Number of active instances."""

    print_symbol = '#'
    """type: Print symbol, any type"""

    def __init__(self, width=0, height=0):
        """Constructor.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return string representation"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.width + '\n') *
                self.height)[:-1]

    def __repr__(self):
        """Return formal string representation"""
        return "Rectangle(" + str(self.__width) +\
            ", " + str(self.__height) + ")"

    def __del__(self):
        """Delete rectangle"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger of two rectangles.

        Args:
            rect_1: first rectangle.
            rect_2: second rectangle.
        Raises:
            TypeError: If rect_1, rect_2 arent instances of class rectangle
        Returns:
            Rectangle with the larger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
