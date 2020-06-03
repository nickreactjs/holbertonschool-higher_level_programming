#!/usr/bin/python3
'''Lookup method module.'''


def lookup(obj):
    '''Look up object attributes and methods.
    Args:
        obj: the object to list.

    Returns:
        list: the list of attributes.
    '''
    return dir(obj)
