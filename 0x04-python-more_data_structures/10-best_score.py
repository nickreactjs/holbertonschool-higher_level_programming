#!/usr/bin/python3


def best_score(a_dictionary):
    kmax = None
    vmax = 0
    if isinstance(a_dictionary, dict):
        for k, v in a_dictionary.items():
            if v > vmax:
                vmax = v
                kmax = k
    return kmax
