#!/usr/bin/python3
from models.rectangle import Rectangle

'''square Class'''


class Square(Rectangle):
    '''Square Class
    This defines a square object that inherits from the
    rectangle class which also inherits from Base model.
    It calls to the super init of rectangle with arguments; size,
    x=0, y=0 and id=None.
    Methods:
        size: A setter and getter methods for size of square
        __str__: A string representation for square object
        update: Assigning values for each attribute
        to_dictionary: Returns a dictionary representation of square object.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Inicilizing ATRIBUTES
        Inheriting attributes ID, width, height, x, y
        Args:
            size (int): size of square
            x (int, optional): horizontal position of square
            y (int, optional): vertical positionn of square
            id (int, optional): unique identifier for object.
        '''
        super().__init__(self, size, x, y, id)

        self.width = size
        self.height = size

    @property
    def size(self):
        '''
        Getter method for size
        Returns:
            int: size of the square object.
        '''
        return self.width

    @size.setter
    def size(self, a):
        '''
        Setter method for size
        Args (int): size of each side of square object.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than one.
        '''
        if not isinstance(a, int):
            raise TypeError('size must be an integer')
        else:
            if a <= 0:
                raise ValueError('size must be > 0')
            else:
                self.width = a
                self.height = a

    def __str__(self):
        '''Method that returns a string representation of square object
        Returns:
            (str):[Square] (<id>) <x>/<y> - <size>
        '''
        t1 = "[Square]"
        t2 = " ({}) {}/{}".format(self.id, self.x, self.y)
        t3 = " - {}".format(self.width)
        return (t1 + t2 + t3)

    def update(self, *args, **kwargs):
        '''Method that assigns a value to each attribute
        Args:
            args (list): A variable list of arguments.
            kwargs (dic): A variable list of keyword arguments.
        '''
        key = ["id", "size", "x", "y"]
        if len(args) > 0:
            for x in range(len(args)):
                setattr(self, key[x], args[x])
        else:
            for a in kwargs:
                setattr(self, a, kwargs[a])

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Square
        Returns:
            (dic): A key:value pairs of attributes.
        '''
        key = ["id", "size", "x", "y"]
        value = [self.id, self.size, self.x, self.y]
        return dict(zip(key, value))
