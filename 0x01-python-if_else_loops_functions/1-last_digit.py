#!/usr/bin/python3
import random
number = random.randint(-10000, 10000) 
num = number % 10
num = num if not num else num - 10 if number < 10 else num
if num > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, num))
elif num < 6 and num != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, num))
else:
    print('Last digit of {} is {} and is 0'.format(number, num))
