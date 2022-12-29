#!/usr/bin/python3

'''
A square object
'''


class Square:
    '''
    The square class, it calculates the area of a square
    '''
    def __init__(self, size=0):
        '''
        Class initializer.
        Args:
            size (int): parameter
        Raises:
            TypeError: raises TypeError if size is not integer
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
            value (int): parameter
        Raises:
            TypeError: raises TypeError if size is not integer
            ValueError: raises ValueError if size is negetive
        Returns:
            int: integer
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

    def my_print(self):
        '''
        A print function to handle printing functionalities
        It prints space  if size is zero
        or '#' to fill the area of the square object
        '''
        if self.__size == 0:
            print()
        else:
            for num in range(self.__size):
                print('#' * self.__size)

    def area(self):
        '''
        Area of square object
        Returns:
            int: area of object
        '''
        return self.__size ** 2
