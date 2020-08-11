#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d2 = []
    for i in my_list:
        if i % 2 == 0:
            d2.append(True)
        else:
            d2.append(False)
    return d2
