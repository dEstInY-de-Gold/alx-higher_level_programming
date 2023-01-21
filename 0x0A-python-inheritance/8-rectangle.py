#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
'''
A rectangle class
'''


class Rectangle(BaseGeometry):
    '''
    Inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        if BaseGeometry.integer_validator(width, width) as e:
            return e
        else:
            self.__width = width
        if BAseGeometry.integer_validator(height, height) as e:
            return e
        else:
            self.__height = height
#        super().integer_validator(name, value)
