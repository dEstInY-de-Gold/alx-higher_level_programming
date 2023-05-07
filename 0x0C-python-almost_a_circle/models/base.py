#!/usr/bin/python3

'''Base Class'''

import json


class Base():
    '''Base Class
    Its the parent class of the model's object classes
    it defines an init method that set id to increment automatically
    if it is not specified in the call to the class
    Methods:
    - to_json_string(list_dictionaries): Returns a json list
        of dictionaries
    - save_to_file(cls, list_objs): save a list of objects to a file
        by class name
    - form_json_steing(json_string): returns a list of dictionaries
    from a  json string representation
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initilizing base module

        Initialises id and sets it to the given value or
        automatically assigns a new value if it is not given
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Converts a list of dictionaries to a json representation

        Args:
            - list_dictionaries: a list of dics
        Returns:
            - A json repr of dict list
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves objects to a file. If file does not exist, it is
        created automatically by the class naming syntax

        Args:
            - cls: class name
            - list_objs: a list of dicts of class objects
        '''
        filename = cls.__name__ + ".json"
        dc = []
        if list_objs:
            for x in list_objs:
                dictionary = x.to_dictionary()
                dc.append(dictionary)
        with open(filename, mode='w', encoding="utf-8") as f:
            s = cls.to_json_string(dc)
            f.write(s)

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns a dict of json strings

        Args:
            - json_string: a json string representation
        Returns:
            A list of json dicts
        '''
        if json_string is None or json_string == "":
            ls = []
            return ls
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Creates a new instance of the calling class with
        attributes specified in a dictionary.

        Args:
            - cls: class name
            - dictionary (dict): A dictionary containing the
            attributes and values to be set on the new instance.

        Returns:
            An instance of the calling class with the attributes
            specified in the dictionary.
        Resaises:
            None
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        loads a JSON file with the name of the class and the
        extension .json, deserializes the JSON data to a list of
        dictionaries using the from_json_string method, creates a
        new object for each dictionary using the create method,
        and returns a list of the new objects.
        Args:
            cls: class name
        Returns:
            A list of object that were deserialised from json data
        '''
        f = cls.__name__ + ".json"
        ls = []
        try:
            with open(f, 'r') as file:
                x = file.read()
                y = cls.from_json_string(x)
                for a in range(len(y)):
                    z = cls.create(**y[a])
                    ls.append(z)
            return ls
        except Exception:
            return ls
