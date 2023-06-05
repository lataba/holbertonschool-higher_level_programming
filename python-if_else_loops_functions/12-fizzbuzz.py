#!/usr/bin/python

def fizzbuzz():

    for number in range(1, 101):
        if ((number % 3 == 0) and (number % 5 == 0)):
            print(f"FizzBuzz", end=' ')
        elif number % 5 == 0:
            print(f"Buzz", end=' ')
        elif number % 3 == 0:
            print(f"Fizz", end=' ')
        else:
            print("{}".format(number), end=' ')
