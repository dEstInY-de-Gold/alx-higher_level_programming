#!/usr/bin/python3

def find_peak(list_of_integers):
    '''
    A function for finding the peak of a list
    '''
    if len(list_of_integers) > 0:
        max = list_of_integers[0]
        for item in list_of_integers:
            if item > max:
                max = item
    else:
        max = None
    return max
