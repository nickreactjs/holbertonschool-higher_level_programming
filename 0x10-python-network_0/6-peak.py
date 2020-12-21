#!/usr/bin/python3
"""Find Peak in integerlist."""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
