#!/usr/bin/python3
'''
Determines if obj is of instance a_class
'''


def is_kind_of_class(obj, a_class):
    '''
    Returns: true if obj is an instance of a_class,
        otherwise, false
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
