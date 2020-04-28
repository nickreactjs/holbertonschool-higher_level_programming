#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = -10
if number >= 0:
    x = 10
lastnumber = number % x
if lastnumber > 5 or lastnumber < -5:
    detail = "and is greater than 5"
elif lastnumber == 0:
    detail = "and is 0"
else:
    detail = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {}".format(number, lastnumber, detail))
