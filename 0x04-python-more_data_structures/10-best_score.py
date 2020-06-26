#!/usr/bin/python3


def best_score(a_dictionary):
    max = 0
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if v > max:
            max = v
            winner = k
    return winner
