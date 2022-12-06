#!/usr/bin/python3


def max_integer(my_list=[]):
    mx = 0
    if len(my_list) < 1:
        return None
    else:
        for num in my_list:
            if num >= mx:
                mx = num
    return mx
