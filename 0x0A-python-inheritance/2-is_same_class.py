#!/usr/bin/python3
'''
Determines object type
'''


def is_same_class(obj, a_class):
    '''
    Returns: true if obj is of type a_class
        otherwise, false
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
