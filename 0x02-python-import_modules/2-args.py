#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 0
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) -1))
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) -1))
    else:
        print("{:d} arguments:".format(len(argv)-1))
    for argument in argv:
        if i != 0:
            print("{:d}: {}".format(i, argument))
        i += 1
