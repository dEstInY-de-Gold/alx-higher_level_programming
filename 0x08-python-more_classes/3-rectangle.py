#!/usr/bin/python3

'''
A rectangle
an object to created from values os width and height
'''


class Rectangle:
    '''
    An object of a rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Initializer
        Args:
            width (int): first parameter
            height (int): second parameter
        Raises:
            TypeError: if either width or height is not int
            ValueError: if either width or height is less than 0
        '''
        self.__width = width
        self.__height = height
    @property
    def width(self, value):
        '''
        Width of rectangle object
        Args:
            value (int): value for width of rectangle
         Raises:
            TypeError: if value is not int
            ValueError: if value is less than 0
        Returns:
            (int): width
        '''
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        else:
            if value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value

    @property
    def height(self):
        '''
        Height of rectangle object
        Args:
            value (int): value for height of rectangle
         Raises:
            TypeError: if value is not int
            ValueError: if value is less than 0
        Returns:
            (int): height
        '''
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        else:
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value

    def area(self):
        '''
        Area of rectangle object
        Returns:
            (int): area
        '''
        return self.__width * self.__height
    def perimeter(self):
        '''
        Perimeter of rectangle object
        Returns:
            (int): perimeter or zero if either
            of width or height is zero
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        '''
        special print method
        prints rectangle to stdout
        '''
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rect = []
            for i in range(self.__height):
                rect.append('{}'.format('#' * self.__width))
        return rect

    def __repr__(self):
        '''
        Return the canonical string representation
        of the rectangle object.
        '''
        return '#'

