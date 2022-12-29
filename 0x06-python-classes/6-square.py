#!/usr/bin/python3

'''
A square object
'''


class Square:
    '''
    the square class
    it calculates the area of a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        The initializer
        Args:
            size (int): first parameter
            position (tuple): second parameter
        Raises:
            TypeError: raised if size or values for position are not ints
            ValueError: raised if size or a similar case found\
                    with position values are negatives
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        if len(position) != 2 or not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            if not isinstance(position[0], int)\
                    or not isinstance(position[1], int):
                raise ValueError('position must be \
                        a tuple of 2 positive integers')
            else:
                self.__position = position

    @property
    def size(self):
        '''
        the getter for value size
        Args:
            value (int): for size
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

    @property
    def position(self):
        '''
        the getter for value position
        Args:
            value (tuple): values used to fill located area with space
        Returns:
            int: given location in a square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                raise ValueError('position must be \
                        a tuple of 2 positive integers')
            else:
                self.__position = value

    def my_print(self):
        '''
        A print function
        prints square object to stdout but fills
        designated areas with a space
        '''
        if self.__size == 0 and self.__position[1] <= 0:
            print()
        else:
            '''
            if self.__position[1] > 0:
                print()
                '''
            for num in range(self.__size):
                cnt = self.__position[0]
                for i in range(self.__size):
                    if cnt > 0:
                        print(' ' * cnt, end='')
                        cnt = 0
                    print('#', end='')
                print()

    def area(self):
        '''
        Area of the square object
        Returns:
            int: area
        '''
        return self.__size ** 2
