#!/usr/bin/python3
""" Base Class Module. """
import json


class Base:
    """ This is the Base Class. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON representation of list_dict. """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [instance.to_dictionary() for instance in list_objs]
        with open("{}.json".format(cls.__name__), "w",
                  encoding="utf-8") as fil:
            fil.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of the JSON string representation
            json string. """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes already set. """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            inst = Rectangle(1, 1)
        elif cls == Square:
            inst = Square(1)
        else:
            inst = None
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances. """
        import os
        jfile = "{}.json".format(cls.__name__)
        if not os.path.isfile(jfile):
            return []
        with open(jfile, 'r', encoding='utf-8') as f:
            return [cls.create(**dic) for dic
                    in cls.from_json_string(f.read())]
