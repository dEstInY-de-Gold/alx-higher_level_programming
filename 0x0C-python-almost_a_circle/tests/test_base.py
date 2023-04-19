#!/usr/bin/python3
"""
unittest to test all the methods of the class
Base to know if the methods are working correctly
"""
import unittest
import pycodestyle
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    """
    A class to test Base Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0,
        "Found code style errors (and warnings).")

    def test_id_as_positive(self):
        """
        Test for positive Base Class id
        """
        base_instance = Base(110)
        self.assertEqual(base_instance.id, 110)
        base_instance = Base(30)
        self.assertEqual(base_instance.id, 30)

    def test_id_as_negative(self):
        """
        Test for negative Base Class id
        """
        base_instance = Base(-20)
        self.assertEqual(base_instance.id, -20)
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)

    def test_id_as_none(self):
        """
        Test for None Base Class id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dict), str)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        with open("Rectangle.json", "r") as file:
            json_string = file.read()
        self.assertEqual(type(json_string), str)

    def test_from_json_string(self):
        json_string = '[{"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}, \
                        {"id": 7, "width": 1, "height": 7, "x": 6, "y": 0}]'
        json_list = Base.from_json_string(json_string)
        self.assertEqual(type(json_list), list)
        self.assertEqual(len(json_list), 2)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)
        self.assertEqual(len(list_rectangles_output), 2)

    def test_create_square(self):
        s1 = Square(5)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(s1 == s2, False)
        self.assertEqual(s1 is s2, False)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_save_to_file_square(self):
        s1 = Square(10)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        with open("Square.json", "r") as file:
            json_string = file.read()
        self.assertEqual(type(json_string), str)

    def test_load_from_file_square(self):
    """Test loading Square objects from file"""
    # Create and save some Square objects to a file
    s1 = Square(5)
    s2 = Square(10)
    Square.save_to_file([s1, s2])

    # Load the Square objects from the file
    loaded_squares = Square.load_from_file()

    # Assert that the loaded objects are of the correct type and have the correct attributes
    self.assertIsInstance(loaded_squares, list)
    self.assertEqual(len(loaded_squares), 2)
    self.assertIsInstance(loaded_squares[0], Square)
    self.assertIsInstance(loaded_squares[1], Square)
    self.assertEqual(loaded_squares[0].size, 5)
    self.assertEqual(loaded_squares[1].size, 10)
