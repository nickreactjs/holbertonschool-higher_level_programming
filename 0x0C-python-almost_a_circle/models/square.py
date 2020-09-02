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

    def update(self, *args, **kwargs):
        """ Update the class. """
        if args:
            n = len(args)
            if n >= 1:
                self.id = args[0]
            if n >= 2:
                self.size = args[1]
            if n >= 3:
                self.x = args[2]
            if n >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """ return a dictionary representation of the square. """
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
