#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        ke = sorted(list(a_dictionary.keys()))
        for i in ke:
            print("{}: {}".format(i, a_dictionary[i]))
