#!/usr/bin/python3


def uniq_add(my_list=[]):
    newlist = set(my_list)
    sum = 0
    for ti in newlist:
        sum += ti
    return sum
