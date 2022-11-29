#!/usr/bin/python3
for c in range(97, 123):
    if chr(c) not in 'eq':
        print(f'{chr(c)}', end = '')
