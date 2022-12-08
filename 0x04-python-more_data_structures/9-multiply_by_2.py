#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    num_item = list(a_dictionary.items())
    for k, v in num_item:
        return k, v * 2
