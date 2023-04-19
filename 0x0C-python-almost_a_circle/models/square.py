#!/usr/bin/python3
'''square Class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square Class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Inicilizating ATRIBUTES
        Inheriting attributes ID, width, height, x, y'''
        super().__init__(size, size, x, y, id)

        self.width = size
        self.height = size

    @property
    def size(self):
        # Preguntar por que es self.width si
        # no estamos definiendo ese parametro
        return self.width

    @size.setter
    def size(self, a):
        if not isinstance(a, int):
            raise TypeError('size must be an integer')
        else:
            if a <= 0:
                raise ValueError('size must be > 0')
            else:
                self.width = a
                self.height = a

    def __str__(self):
        '''Method that returns
        [Square] (<id>) <x>/<y> - <size>'''
        t1 = "[Square]"
        t2 = " ({}) {}/{}".format(self.id, self.x, self.y)
        t3 = " - {}".format(self.width)
        return (t1 + t2 + t3)

    def update(self, *args, **kwargs):
        '''Method that assigns a value to each attribute'''
        key = ["id", "size", "x", "y"]
        if len(args) > 0:
            for x in range(len(args)):
                setattr(self, key[x], args[x])
        else:
            for a in kwargs:
                setattr(self, a, kwargs[a])

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Square'''
        key = ["id", "size", "x", "y"]
        value = [self.id, self.size, self.x, self.y]
        return dict(zip(key, value))
