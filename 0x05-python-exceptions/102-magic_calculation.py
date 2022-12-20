#!/usr/bin/python3
import sys


def magic_calculation(a, b):
    for ch in sys.args[]:
        try:
            return a ch b
        except Exception as exc:
            raise exc
