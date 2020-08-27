#!/usr/bin/python3
"""Same class or inherit from module."""


def is_kind_of_class(obj, a_class):
    """ Check if is instance."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
