#!/usr/bin/python3


def common_elements(set_1, set_2):
    common = []
    for ti in set_1:
        if ti in set_2:
            common.append(ti)
    return common
