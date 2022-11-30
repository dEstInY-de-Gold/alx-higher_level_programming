#!/usr/bin/python3

def uppercase(str):
    length = 0
    for c in str:
        length += 1
        if 65 <= ord(c) <= 90:
            c = c
        elif 97 <= ord(c) < 122:
            c = chr(ord(c) - 32)
        if length < len(str):
            print('{}'.format(c), end = '')
        else:
            print('{}'.format(c))
