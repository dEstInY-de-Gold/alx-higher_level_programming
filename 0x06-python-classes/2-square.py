#!/usr/bin/python3


class Square:
    '''
    Square 
    __init__
    raises a ValueError or TypeError if a wrong value is entered
    Args:
        size: parameter
    '''
    def __init__(self, size=0):
        if (isinstance(size, int)) != True:
            raise ValueError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size


if __name__ == '__main__':
    Square.main()
