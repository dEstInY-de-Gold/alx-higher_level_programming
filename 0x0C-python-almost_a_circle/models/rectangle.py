#!/usr/bin/python3
from models.base import Base

'''
Rectangle class inheritting from Base class
'''


class Rectangle(Base):
    '''
    Inherits from Base class
    This class defines private attribute for the folowing;
    height: the height of the rectangle object
    widh: the width of the rectangle object

    it also inherits from the base module's properties
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialiser
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int, optional): horizontal position of the rectangle.
                Defaults to 0.
            y (int, optional): vertical position of the rectangle.
                Defaults to 0.
            id (int, optional): unique identifier for the instance.
                If not provided, the value of __nb_objects will be used
                and incremented.

        Raises:
            TypeError: if width, height, x, or y are not integers.
            ValueError: if width, height, x, or y are less than or
                equal to 0.
        '''
        # calling init method for super class
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
        Gets the width of the Rectangle object.

        Returns:
            int: The width of the Rectangle object.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Width method for rectangle
        Args: value (int): size of width
        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 1
        '''
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
        Return (int): size of heght
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Height of rectangle
        Args: value (int): size of height
        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 1
        '''
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
        Gets the x-coordinate of the Rectangle object.

        Returns:
            int: The x-coordinate of the Rectangle object.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        x - value of other instance attributes
        Args: value (int): the given value
        Raises:
            ValueError: if value is less than 1
        '''
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
        Gets the y-coordinate of the Rectangle object.

        Returns:
            int: The y-coordinate of the Rectangle object.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        y - value of y-instance attribute
        Args: value (int): the given value
        Raises:
            ValueError: if value is less than 1
        '''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        else:
            if value < 0:
                raise ValueError('y must be >= 0')
            else:
                self.__y = value

    def area(self):
        '''
        Defines the area of the object
        Return (int): the area
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Prints a special formatted display of the object
        '''
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            spc = self.__width * '#'
            x_axes = self.__x * ' '
            print('{}{}'.format(x_axes, spc))

    def __str__(self):
        '''A customised string format
        Returns (str): the string
        '''
        prnt = f'[Rectangle] ({self.id}) {self.__x}/\
                {self.__y} - {self.__width}/{self.__height}'
        return prnt

    def update(self, *args, **kwargs):
        '''Method that assigns a value to each attribute
        Args:
            args: a variable list of arguments for height, width,
                x, y and id values for the rectangle object.
            kwargs (dict): also a variable list of arguments
                but in dic format
        '''
        if len(args) > 0:
            key = ["id", "width", "height", "x", "y"]
            for x in range(len(args)):
                setattr(self, key[x], args[x])
        if len(args) == 0:
            for x in kwargs:
                setattr(self, x, kwargs[x])

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Rectangle
        Returns:
            A dictionary representation of rectangle object
        '''
        key = ["id", "width", "height", "x", "y"]
        value = list(self.__dict__.values())
        return dict(zip(key, value))
