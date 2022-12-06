#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        mx = my_list[0]
        for num in my_list:
            if num >= mx:
                mx = num
    return mx
