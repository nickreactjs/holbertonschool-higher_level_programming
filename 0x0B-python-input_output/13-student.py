#!/usr/bin/python3
"""Student to JSON Module. """


class Student:
    """ Student class. """

    def __init__(self, first_name, last_name, age):
        """ INIT """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve a dictionary represantion of a Student instance """
        check = 0
        if type(attrs) is list:
            for i in attrs:
                if not isinstance(i, str):
                    check = 1
        else:
            check = 1
        if check == 0:
            adic = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    adic[k] = v
            return adic
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """ Replace all attributes of the Student instance. """
        for k, v in json.items():
            self.k = v
