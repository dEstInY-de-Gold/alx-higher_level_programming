#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        newlist = my_list[:idx] + my_list[idx + 1:]
        my_list.clear()
        for num in newlist:
            my_list.append(num)
    return my_list
