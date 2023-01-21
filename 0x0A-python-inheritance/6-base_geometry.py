#!/usr/bin/python3
'''
Base geometry
'''


class BaseGeometry:
    '''
    Non-implemented area
    '''
    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')
