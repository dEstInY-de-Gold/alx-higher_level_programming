#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    else:
        mx = ''
        for item in a_dictionary:
            if item >= mx:
                mx = item
    return mx
