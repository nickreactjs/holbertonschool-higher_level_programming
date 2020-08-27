#!/usr/bin/python3
"""Module is same class"""


def is_same_class(obj, a_class):
    """Check if obj is same class."""
    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return True
        else:
            return False
