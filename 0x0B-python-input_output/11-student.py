#!/usr/bin/python3
"""Student to JSON Module. """


class Student:
    """ Student class. """

    def __init__(self, first_name, last_name, age):
        """ INIT """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieve a dictionary represantion of a Student instance """
        return self.__dict__.copy()
