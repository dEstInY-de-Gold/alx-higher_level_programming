#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        if (isinstance(size, int) != True):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def size(self, value):
        self.value = value
        '''
        if isinstance(value, int) != True:
            raise TypeError('value must be an integer')
        else:
            if value < 0:
                raise ValueError('value must be >= 0')
            else:
                self.value = value
'''
    def size(self):
        return self.value

    def area(self):
        return self.__size ** 2
 
