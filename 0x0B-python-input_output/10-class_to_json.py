#!/usr/bin/python3
""" Class to JSON Module. """
import json


def class_to_json(obj):
    """ Return the dictionary description with simple data data
        structure for JSON serialization of an object. """
    if hasattr(obj, '__dict__'):
        return obj.__dict__.copy()
    else:
        return {}
