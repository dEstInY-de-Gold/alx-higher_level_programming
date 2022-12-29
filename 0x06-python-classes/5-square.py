#!/usr/bin/python3


class Square:
    '''
    the square class
    it calculates the area of a square
    '''
    def __init__(self, size=0):
        if (isinstance(size, int) not True):
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
        Returns: integer
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) not True:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for num in range(self.__size):
                print('#' * self.__size)

    def area(self):
        return self.__size ** 2
