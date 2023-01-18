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
