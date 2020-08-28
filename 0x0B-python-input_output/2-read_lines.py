#!/usr/bin/python3
""" Read n lines Module. """


def read_lines(filename="", nb_lines=0):
    nb = 0
    with open(filename, 'r') as f:
        for line in f:
            if nb >= nb_lines and not nb_lines <= 0:
                break
            print(line, end='')
            nb += 1
