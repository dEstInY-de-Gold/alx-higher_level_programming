#!/usr/bin/python3

'''
Definition of a square object.
'''


class Square:
    '''
    Square class object
    '''
    def __init__(self, size=0):
        '''
        Initializer for square class.
        Args:
            size (int): parameter
        Raises:
            ValueError: raises a ValueError if size is negative
            TypeError: raises TypeError if size is not an integer
        '''
        if not (isinstance(size, int)):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
