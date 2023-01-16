#!/usr/bin/python3

'''
Base class
'''


class Base:
    '''
    Base class for other tasks
    in this project
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
