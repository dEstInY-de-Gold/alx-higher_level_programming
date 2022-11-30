#!/usr/bin/python3

def uppercase(str):
    length = 0
    for c in str:
        length += 1
        if (ord(c) < 65 or ord(c) > 90) and (97 <= ord(c) < 122):
            c = chr(ord(c) - 32)
        if length < len(str):
            print('{}'.format(c), end = '')
        else:
            print('{}'.format(c))
