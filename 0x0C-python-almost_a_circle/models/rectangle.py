#!/usr/bin/python3
from models.base import Base

'''
Rectangle class inheritting from Base class
'''


class Rectangle(Base):
    '''
    Inherits from Base class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialiser
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): other instance attribute
            y (int): another instance attributes
        '''
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        else:
            if width <= 0:
                raise ValueError('width must be > 0')
            else:
                self.width = width
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        else:
            if height <= 0:
                raise ValueError('height must be > 0')
            else:
                self.height = height
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        else:
            if x < 0:
                raise ValueError('x must be >= 0')
            else:
                self.x = x
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        else:
            if y < 0:
                raise ValueError('y must be >= 0')
            else:
                self.y = y

    @property
    def width(Self):
        '''
        Width method of rectangle
        Args: value (int): size of width
        Raises:
            TypeError: if value is not an int
            ValueError: if value is not greater than 0 
        '''
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        else:
            if value <= 0:
                raise ValueError('width must be > 0')
            else:
                self.__width = value

    @property
    def height(self):
        '''
        height of rectangle
        Args: height (int): size of height
        Raises:
            TypeError: if value is not an int
            ValueError: if value is not greater than 0
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        else:
            if value <= 0:
                raise ValueError('height must be > 0')
            else:
                self.__height = value

    @property
    def x(self):
        '''
        x - value of other instance attributes
        Args: x (int): other instance attribute
        Raises:
            ValueError: if value is not greater than 0
        '''
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        else:
            if value < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__x = value

    @property
    def y(self, value):
        '''
        y - value of other instance attribute
        Args: value (int): y
        Raises:
            ValueError: if value is not greater than 0
        '''
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        else:
            if value < 0:
                raise ValueError('y must be >= 0')
            else:
                self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            spc = self.__width * '#'
            x_axes = self.__x * ' '
            print('{}{}'.format(x_axes, spc))

    def __str__(self):
        '''A customised string format
        Returns: the string
        '''
        prnt = f'[Rectangle] ({self.id}) {self.__x}/'\
                f'{self.__y} - {self.__width}/{self.__height}'
        return prnt

    def update(self, *args, **kwargs):
        '''Method that assigns a value to each attribute'''
        # Manera en la cual creas una lista con cada nombre de cada
        # atributo y busca su existencia en el objeto
        if len(args) > 0:
            key = ["id", "width", "height", "x", "y"]
            for x in range(len(args)):
                setattr(self, key[x], args[x])
        # Manera en la cual busca todos los attributos del objeto
        # y los convierte en una lista
        if len(args) == 0:
            for x in kwargs:
                setattr(self, x, kwargs[x])

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Rectangle'''
        key = ["id", "width", "height", "x", "y"]
        value = list(self.__dict__.values())
        return dict(zip(key, value))
