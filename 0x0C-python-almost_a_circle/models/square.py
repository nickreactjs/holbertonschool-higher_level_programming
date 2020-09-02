#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class. """

    def __init__(self, size, x=0, y=0, id=None):
        """ super().__init__() """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str and print. """
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ property and setter. """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
