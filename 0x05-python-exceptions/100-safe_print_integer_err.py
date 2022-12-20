#!/usr/bin/python3


def safe_print_integer_err(value):
    ret = False
    try:
        print('{:d}'.format(value))
        ret = True
    except ValueError:
        message = "Unknown format code 'd' for object of type 'str'"
        print('Exception: {}'.format(message))
    return ret
