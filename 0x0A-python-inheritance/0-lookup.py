#!/usr/bin/python3

""" lookup task """

def lookup(obj):
    """
    returns the list of available attributes and methods of an object.
    Args:
        obj (dic): A dictionary object as input.
    Returns: (list): A list of available attributes and methods of an object.
    """
    return dir(obj)
