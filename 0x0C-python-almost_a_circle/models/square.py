#!/usr/bin/python3
from models.rectangle import Rectangle
"""Square Module"""


class Square(Rectangle):
    """ Square class. """

    def __init__(self, size, x=0, y=0, id=None):
        """ super().__init__() """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str and print. """
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.height)
