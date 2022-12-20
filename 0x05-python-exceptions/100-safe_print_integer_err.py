#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    ret = False
    try:
        print('{:d}'.format(value))
        ret = True
    except ValueError:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return ret
