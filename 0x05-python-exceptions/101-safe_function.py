#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as err:
        sys.stderr, 'Exception: ', err
        return None
    return res
