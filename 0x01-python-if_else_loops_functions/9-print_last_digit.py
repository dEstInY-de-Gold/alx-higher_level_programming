#!/usr/bin/python3

def print_last_digit(number):
    num = number % 10
    num = num if not num else num-10 if number<10 else num
    num = abs(num)
    print('{}'.format(num), end = '')
    return num
