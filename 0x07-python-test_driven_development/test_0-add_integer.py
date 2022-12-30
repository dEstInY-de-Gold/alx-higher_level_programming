#!/usr/bin/python3
import unittest
import 0-add_interger


class testAdd(unittest.TestCase):
    def test_add_integer(self):
        t = 0-add_integer.add_integer
        self.assertEqual(t(5, 10), 15)
        self.assertEqual(t(-2, 20), 18)
        self.assertEqual(t(-5, -16, -21))


if __name__ == '__main__':
    unittest.main()
