#!/usr/bin/python3
""" A module of unit test"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class testClass(unittest.TestCase):
    """A test class"""

    def test_func(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
