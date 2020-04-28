#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = -10
if number >= 0:
    x = 10
lastnumber = number % x
if lastnumber > 5:
    detail = "greater than 5"
elif lastnumber == 0:
    detail = "0"
else:
    detail = "less than 6 and not 0"
sentence = "Last digit of {:d} is {:d} and is {}"
print(sentence.format(number, lastnumber, detail))
