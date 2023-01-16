#!/usr/bin/python3
from models.base import Base

'''
Rectangle class inheritting from Base class
'''


class Rectangle(Base):
    '''
    Inherits from Base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialiser
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): other instance attribute
            y (int): another instance attributes
        '''
        super().__init__(self)
        self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(Self):
        '''
        Width method of rectangle
        Args: value (int): size of width
        '''
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''
        height of rectangle
        Args: height (int): size of height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''
        x - value of other instance attributes
        Args: x (int): other instance attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self, value):
        '''
        y - value of other instance attribute
        Args: value (int): y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
