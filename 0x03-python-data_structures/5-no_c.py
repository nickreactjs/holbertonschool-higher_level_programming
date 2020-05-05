#!/usr/bin/python3
def no_c(my_string):
    strlen = len(my_string)
    i = 0
    while i < strlen:
        if my_string[i] == 'C' or my_string[i] == 'c':
            my_string = my_string[:i] + my_string[i + 1:]
            strlen -= 1
        i += 1
    return (my_string)
