#!/usr/bin/python3
while (1 <=  i <= 98):
    if i % 10 == 0:
        i += (i / 10) + 1
        continue
    if i < 98:
        print(f'{i:02}, ', end = '')
    else:
        print(f'{i}')
    i += 1
