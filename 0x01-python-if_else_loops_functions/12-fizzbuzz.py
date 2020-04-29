#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if not(i % 5) and not(i % 3):
            print("{}".format("FizzBuzz"), end=' ')
        elif not(i % 3):
            print("{}".format("Fizz"), end=' ')
        elif not(i % 5):
            print("{}".format("Buzz"), end=' ')
        else:
            print("{:d}".format(i), end=' ')
