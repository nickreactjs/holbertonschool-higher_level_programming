#!/usr/bin/python3
""" Write to a file module. """


def write_file(filename="", text=""):
    """ Write a string to a tesxt file and
    return the number of chars written. """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
