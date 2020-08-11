#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = [i for i in set_1 if not i in set_2]
    b = [i for i in set_2 if not i  in set_1]
    return set(a + b)
