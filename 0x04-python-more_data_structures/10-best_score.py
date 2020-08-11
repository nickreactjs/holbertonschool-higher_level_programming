#!/usr/bin/python3
def best_score(a_dictionary):
    maxv = -9999999
    maxk = None
    if a_dictionary is None:
        return None
    for k, v in a_dictionary.items():
        if v > maxv:
            maxk = k
            maxv = v
    return maxk
