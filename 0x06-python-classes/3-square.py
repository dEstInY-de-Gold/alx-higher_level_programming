#!/usr/bin/python3


class Square:
    '''
    A class square.
    '''
    def __init__(self, size=0):
        '''
        Class initializer method
        Args:
            size: parameter
        Raises:
            TypeError: raises TypeError is size is not an integer
            ValueError: raises ValueError if size is negative
        '''
        if (isinstance(size, int) not True):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        '''
        Area of the square is calculated
        Returns:
            int: square of object
        '''
        return self.__size ** 2
