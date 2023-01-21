#!/usr/bin/python3
'''
Base geometry
'''


class BaseGeometry:
    '''
    Non-implemented area
    '''
    def __init__(self, name=None, value=0):
        pass
    '''
        self.name = name
        self.value = value

'''
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
