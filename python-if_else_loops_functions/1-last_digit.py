#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
print("Last digit of", '{:d}'.format(number), "is", '{:d}'.format(last), end=" ")
if last > 5:
    print("and is greater than 5")
elif (last < 6) and (last != 0):
    print("and is less than 6")
else:
    print("and is 0")
