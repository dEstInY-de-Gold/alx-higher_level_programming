#!/usr/bin/python3

'''
prints a square with the character #
'''


def print_square(size):
    '''
    fills area of a square with the
    character '#' to the screen
    Args:
        size (int): size of the square
    Raises:
        TypeError: raises a TypeError if
        size is not an integer value.
        size must also not be a negative
        value or a float value
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be >= 0')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
