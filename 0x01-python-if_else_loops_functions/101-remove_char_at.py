#!/usr/bin/python3
def remove_char_at(str, n):
    if 0 <= n <= len(str):
        strnew = str[:n] + str[n + 1:]
        return strnew
    return str
