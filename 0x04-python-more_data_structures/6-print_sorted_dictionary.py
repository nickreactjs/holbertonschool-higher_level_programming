#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sd = sorted(a_dictionary)
    for ti in sd:
        print("{}: {}".format(ti, a_dictionary[ti]))
