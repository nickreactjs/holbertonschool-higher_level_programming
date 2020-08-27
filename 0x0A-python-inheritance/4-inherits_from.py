#!/usr/bin/python3
""" Only sub class of Module."""


def inherits_from(obj, a_class):
    """ Check if is subclass. """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
