#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    diff = []
    for ti in set_1:
        if ti not in set_2:
            diff.append(ti)
    for ti1 in set_2:
        if ti1 not in set_1:
            diff.append(ti1)
    return diff

