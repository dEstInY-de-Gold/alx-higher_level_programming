#!/usr/bin/python3


class Square:
    '''
    the square class
    it calculates the area of a square
    '''
    def __init__(self, size=0, position = (0, 0)):
        '''
        self.__size = size
        self.__position = position
        '''
        if (isinstance(size, int) != True):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        if len(position) != 2 or type(position) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            if isinstance(position[0], int) != True or isinstance(position[1], int) != True:
                raise ValueError('position must be a tuple of 2 positive integers')
            else:
                self.__position = position

    @property    
    def size(self):
        '''
        the getter for value size
        Returns: integer
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

    @property    
    def position(self):
        '''
        the getter for value position
        Returns: given location in a square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            if isinstance(value[0], int) != True or isinstance(value[1], int) != True:
                raise ValueError('position must be a tuple of 2 positive integers')
            else:
                self.__position = value


    def my_print(self):
        if self.__size == 0 and self.__position[1] <= 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for num in range(self.__size):
                cnt = self.__position[0]
                for i in range(self.__size):
                    if cnt > 0:
                        print(' ' * cnt, end='')
                        cnt = 0
                    print('#', end='')
                print()

    def area(self):
        return self.__size ** 2 