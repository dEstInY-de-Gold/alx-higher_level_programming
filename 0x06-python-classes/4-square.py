#!/usr/bin/python3

'''
A square object
'''


class Square:
    '''
    the square class
    it calculates the area of a square
    '''
    def __init__(self, size=0):
        '''
        Args:
            size (int): parameter
        Raises:
            TypeError: raises TypeError if size is not an int
            ValueError: raises ValueError if size is negetive
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    @property
    def size(self):
        '''
        the getter for value size
        Args:
            value (int): integer value for size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size a negative value
        Returns:
            int: integer value for size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        '''
        Area of square
        Returns:
            int: square of the defined object
        '''
        return self.__size ** 2
