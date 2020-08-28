#!/usr/bin/python3
""" Read file module. """


def read_file(filename=""):
    """ read a text file and print it to stdout. """
    with open(filename) as f:
        for line in f:
            print(line, end='')
