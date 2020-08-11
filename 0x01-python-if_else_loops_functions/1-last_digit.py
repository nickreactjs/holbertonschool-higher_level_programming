#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if ld > 5:
    word = "and is greater than 5"
elif ld == 0:
    word = "and is 0"
elif ld < 6:
    word = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, ld, word))
