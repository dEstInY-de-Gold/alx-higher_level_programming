#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sumd = 0
    count = 0
    for x in my_list:
        sumd += x[0] * x[1]
        count += x[1]
    return sumd / count
