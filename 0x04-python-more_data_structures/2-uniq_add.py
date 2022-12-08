#!/usr/bin/python3


def uniq_add(my_list=[]):
    sumd = 0
    no_duplicate = []
    for i in my_list:
        if i not in no_duplicate:
            sumd += i
            no_duplicate.append(i)
    return sumd
