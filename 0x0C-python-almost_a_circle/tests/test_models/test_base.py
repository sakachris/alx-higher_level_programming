#!/usr/bin/python3
"""
test_models/base.py for testing Base class
"""
import unittest
from models.base import Base
import pycodestyle


class TestBase(unittest.TestCase):
    """
    Testing for Base Class
    """
    def test_documentation(self):
        self.assertTrue(len(Base.__doc__) >= 20, "Short or no documentation")

    def test_pycodestyle(self):
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/base.py',
                                     'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        base1 = Base()
        self.assertIsInstance(base1, Base, "Not instance of Base")

    def test_id(self):
        """
        Testing id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(20)
        b4 = Base()
        b5 = Base(-5)
        b6 = Base()
        b7 = Base(None)
        b8 = Base(0)
        b9 = Base('one')
        b10 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 20)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 4)
        self.assertEqual(b7.id, 5)
        self.assertEqual(b8.id, 0)
        self.assertEqual(b9.id, 'one')
        self.assertEqual(b10.id, 6)
