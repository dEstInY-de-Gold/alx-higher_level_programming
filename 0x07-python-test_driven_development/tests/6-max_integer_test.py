#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    A tesy case for finding max number in a list
    '''
    def test_max_integer(self):
        '''
        The initializer for testing max int
        '''
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([0, -9, -1002, -0.55, -0.5]), 0)
        self.assertEqual(max_integer([3 * 3, 7 / 6, 322 % 100, 0, 2 ** 9]), 512)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -9, -9000000, -0.11114, -0.1111112]), -0.1111112)
