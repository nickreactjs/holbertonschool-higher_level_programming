#!/usr/bin/python3
""" Rectangle Module. """
from models.base import Base


class Rectangle(Base):
    """ Class Retangle that inherits from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ INIT"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter and setter. """
        return self.__width

    @width.setter
    def width(self, width):
        self.validate_int("width", width)
        self.__width = width

    @property
    def height(self):
        """ Property and setter """
        return self.__height

    @height.setter
    def height(self, height):
        self.validate_int("height", height)
        self.__height = height

    @property
    def x(self):
        """ Property and setter. """
        return self.__x

    @x.setter
    def x(self, x):
        self.validate_int("x", x)
        self.__x = x

    @property
    def y(self):
        """ Property of y and setter. """
        return self.__y

    @y.setter
    def y(self, y):
        self.validate_int("y", y)
        self.__y = y

    def validate_int(self, attribute, input):
        """ Validate integer. """
        if not isinstance(input, int):
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "width" or attribute == "height":
            if input <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        else:
            if input < 0:
                raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """ Return area value. """
        return self.width * self.height

    def display(self):
        """ Print in stdout the Rectangle instance with
        the character #"""
        row = ' ' * self.x + "#" * self.width + '\n'
        print('\n' * self.y + row * self.height, end='')

    def __str__(self):
        """ Str and print()"""
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """ Assign an argument to each attribute """
        na = len(args)
        if na >= 1:
            self.id = args[0]
        if na >= 2:
            self.width = args[1]
        if na >= 3:
            self.height = args[2]
        if na >= 4:
            self.x = args[3]
        if na >= 5:
            self.y = args[4]
