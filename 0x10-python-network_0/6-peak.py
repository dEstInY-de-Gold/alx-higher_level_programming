#!/usr/bin/python3

'''
Peak in a list
'''


def find_peak(list_of_integers):
    '''
    A function for finding the peak of a list
    '''
    '''
    if len(list_of_integers) > 0:
        max = list_of_integers[0]
        for item in list_of_integers:
            if item > max:
                max = item
    else:
        max = None
        '''
    if len(list_of_integers) == 0:
        return None

    for item in list_of_integers:
        indx = list_of_integers.index(item)
        if indx < 1:
            prev_item = 0
        else:
            prev_item = list_of_integers[indx-1]

        if (len(list_of_integers) - 1) == indx:
            next_item = 0
        else:
            next_item = list_of_integers[indx+1]
        if item >= prev_item and item >= next_item:
            pk = item
    return pk
