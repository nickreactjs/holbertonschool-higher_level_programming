#!/usr/bin/python3
""" Number of lines module. """


def number_of_lines(filename=""):
    """ Return number of lines in a file. """
    lines = 0
    with open(filename, 'r') as f:
        for _ in f:
            lines += 1
    return lines
