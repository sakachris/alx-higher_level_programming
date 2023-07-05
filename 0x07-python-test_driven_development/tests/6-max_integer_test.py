#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Testing for maximum integer
    """
    def test_with_int(self):
        """
        Test using integers
        """
        self.assertEqual(max_integer([-4, 2, 0, 8]), 8)
        self.assertEqual(max_integer([-4, -1, -8]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer((50, 40, 30)), 50)

    def test_non_int(self):
        """
        Test using non-integers
        """
        self.assertEqual(max_integer([2.9, 2.999, 2.99]), 2.999)
        self.assertEqual(max_integer([-0.1, -0.01, -0.001]), -0.001)
        self.assertEqual(max_integer(['one', 'two', 'three', 'four']), 'two')
        self.assertEqual(max_integer(('3', '1', '4', '2')), '4')
        self.assertEqual(max_integer([{1, 2, 3}, {1, 2}]), {1, 2, 3})
        self.assertEqual(max_integer([(1, 2, 3), (1, 2)]), (1, 2, 3))
        self.assertEqual(max_integer('7'), '7')

    def test_empty(self):
        """
        Test empty or no list
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_raises(self):
        """
        Test for errors
        """
        self.assertRaises(TypeError, max_integer, {1, 2, 3})
        self.assertRaises(TypeError, max_integer, (1))
        self.assertRaises(TypeError, max_integer, ['one', 2, 'three'])
        self.assertRaises(TypeError, max_integer, 6)
