#!/usr/bin/python3
""" To JSON string Module."""
import json


def to_json_string(my_obj):
    """ Return the json representaion of an object. """
    return json.dumps(my_obj)
