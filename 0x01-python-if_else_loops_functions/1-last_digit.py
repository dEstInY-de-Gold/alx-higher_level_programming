#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
num = number % 10
s = 'Last digit of '
num = num if not num else num - 10 if number < 10 else num
if num > 5:
    print('{}{} is {} and is greater than 5'.format(s, number, num))
elif num < 6 and num != 0:
    print('{}{} is {} and is less than 6 and not 0'.format(s, number, num))
else:
    print('{}{} is {} and is 0'.format(s, number, num))
