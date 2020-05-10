#!/usr/bin/python3


def roman_to_int(roman_string):
    rint = 0
    if roman_string and isinstance(roman_string, str):
        for ti in roman_string:
            if ti == 'X':
                rint += 10
            elif ti == 'V':
                rint += 5
            elif ti == 'I':
                rint += 1
            elif ti == "L":
                rint += 50
            elif ti == 'D':
                rint += 500
            elif ti == 'C':
                rint += 100
    return rint
