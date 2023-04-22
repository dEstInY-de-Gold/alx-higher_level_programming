#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import re


def methods_base():
    print('BASE ' * 5)
    print(Base.__doc__)
    funcs = ('__init__', 'to_json_string', 'save_to_file', 'from_json_string', 'create', 'load_from_file')
    func_dic = {
            '__init__': Base.__init__,
            'to_json_string': Base.to_json_string,
            'save_to_file': Base.save_to_file,
            'from_json_string': Base.from_json_string,
            'create': Base.create,
            'load_from_file': Base.load_from_file
            }
    for func in funcs:
        if func in func_dic:
            print(func.__doc__)

def methods_rect():
    print('RECTANGLE ' * 5)
    funcs = ('__init__', 'width', 'height', 'x', 'y', 'area', 'display', '__str__', 'update', 'to_dictionary')
    func_dic = {
            '__init__': Rectangle.__init__,
            'width': Rectangle.width,
            'heght': Rectangle.height,
            'x': Rectangle.x,
            'y': Rectangle.y,
            'area': Rectangle.area,
            'display': Rectangle.display,
            '__str__': Rectangle.__str__,
            'update': Rectangle.update,
            'to_dictionary': Rectangle.to_dictionary
            }
    for func in funcs:
        if func in func_dic:
            print(func.__doc__)

def methods_square():
    print('SQUARE ' * 5)
    funcs = ('__init__', 'size', '__str__', 'update', 'to_dictionary')
    func_dic = {
            '__init__': Square.__init__,
            'size': Square.size,
            '__str__': Square.__str__,
            'update': Square.update,
            'to_dictionary': Square.to_dictionary
            }
    for func in funcs:
        if func in func_dic:
            print(func.__doc__)


if __name__ == "__main__":
    methods_base()
    print()
    print('#*#' * 25)
    print()
    methods_rect()
    print()
    print('#*#' * 25)
    print()
    methods_square()
