#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for num in range(x):
        try:
            print('{:d}'.format(my_list[num]), end='')
            length += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print()
    return length
