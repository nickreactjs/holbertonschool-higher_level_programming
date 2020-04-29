#!/usr/bin/python3
def uppercase(str):
    upper = []
    for letter in str:
        if 97 <= ord(letter) <= 122:
            character = chr(ord(letter) - 32)
        else:
            character = letter
        print("{}".format(character), end='')
    print()
