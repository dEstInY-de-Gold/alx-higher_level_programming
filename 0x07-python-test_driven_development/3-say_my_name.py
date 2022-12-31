#!/usr/bin/python3

'''
A function that says your name
'''


def say_my_name(first_name, last_name=""):
    '''
    It will print name as give otherwise
    raises an error appropriately
    Args:
        first_name (str): first name
        last_name (str): last name
    Raises:
        TypeError: raised if inputs are not strings
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('my name is {} {}'.format(first_name, last_name))
