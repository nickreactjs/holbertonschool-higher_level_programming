#!/usr/bin/python3
def uppercase(str):
    for v in str:
        ch = ord(v)
        if 96 < ch < 123:
            ch = ch - 32
        print("{}".format(chr(ch)), end="")
    print()
