#!/usr/bin/python3
'''
Determines if obj is of instance a_class
'''


def inherits_from(obj, a_class):
    '''
    Returns: true if obj is an instance of a_class,
        otherwise, false
    '''
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
