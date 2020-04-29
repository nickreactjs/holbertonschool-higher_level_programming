#!/usr/bin/python3
def uppercase(str):
    upper = []
    for letter in str:
        if 97 <= ord(letter) <= 122:
            print(chr(ord(letter) - 32), end='')
        else:
            print(letter, end='')
    print()
