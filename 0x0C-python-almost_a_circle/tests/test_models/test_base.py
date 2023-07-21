#!/usr/bin/python3
"""
test_models/base.py for testing Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pycodestyle
import os


class TestBase(unittest.TestCase):
    """
    Testing for Base Class
    """
    def test_documentation(self):
        """ tests for documentation """
        self.assertTrue(len(Base.__doc__) >= 20, "Short or no documentation")
        self.assertTrue(len(Base.to_json_string.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.save_to_file.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.from_json_string.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.create.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.load_from_file.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Base.save_to_file_csv.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ tests for pycodestyle """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/base.py',
                                     'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ tests for instance """
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

    def test_to_json_string(self):
        """ Tests conversion to json_string """
        dlist = [{'width': 10, 'height': 5, 'x': 2, 'y': 1, 'id': 1}]
        jstr = Base.to_json_string(dlist)
        ejstr = '[{"width": 10, "height": 5, "x": 2, "y": 1, "id": 1}]'
        self.assertEqual(jstr, ejstr)
        self.assertIsInstance(jstr, str)

        dlist2 = [{'size': 10, 'x': 2, 'y': 1, 'id': 1}]
        jstr2 = Base.to_json_string(dlist2)
        ejstr2 = '[{"size": 10, "x": 2, "y": 1, "id": 1}]'
        self.assertEqual(jstr2, ejstr2)
        self.assertIsInstance(jstr2, str)

        dlist3 = []
        jstr3 = Base.to_json_string(dlist3)
        ejstr3 = '[]'
        self.assertEqual(jstr3, ejstr3)
        self.assertIsInstance(jstr3, str)

        dlist4 = None
        jstr4 = Base.to_json_string(dlist4)
        ejstr4 = '[]'
        self.assertEqual(jstr4, ejstr4)
        self.assertIsInstance(jstr4, str)

    def test_save_to_file(self):
        """ Tests saving to json file """
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(3, 4)
        Base.save_to_file([self.r1, self.r2])
        self.assertTrue(os.path.isfile('Rectangle.json'))

        self.s1 = Square(1, 2)
        self.s2 = Square(3, 4)
        Base.save_to_file([self.s1, self.s2])
        self.assertTrue(os.path.isfile('Square.json'))
