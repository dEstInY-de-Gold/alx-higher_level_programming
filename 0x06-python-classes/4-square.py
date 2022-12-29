#!/usr/bin/python3


class Square:
    '''
    the square class
    it calculates the area of a square
    '''
    def __init__(self, size=0):
        '''
        Args:
            size (int): parameter
        '''
        if (isinstance(size, int) != True):
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
        if isinstance(value, int) != True:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        return self.__size ** 2
 
