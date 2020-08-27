#!/usr/bin/python3
""" Module for Rectangle. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is the Rectangle class that inherits from BaeGeometry. """

    def __init__(self, width, height):
        """ Init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__widht = width
        self.__height = height
