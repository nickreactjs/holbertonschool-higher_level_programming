#!/usr/bin/python3
"""Lookup method module."""

def lookup(obj):
    """ Print all attributes and methods.
    Args:
        obj
    Returns:
        list
    """
    return list(dir(obj))
