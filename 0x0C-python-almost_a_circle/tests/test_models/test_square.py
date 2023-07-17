#!/usr/bin/python3
"""
test_models/rectangle.py for testing Rectangle class
"""
import unittest
import io
from contextlib import redirect_stdout
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class TestBase(unittest.TestCase):
    """
    Testing for Base Class
    """
    def setUp(self):
        Base._Base__nb_objects = 0
        self.s1 = Square(10, 5, 2, 11)
        self.s2 = Square(4, 4, 1)
        self.s3 = Square(3, 2, 2)

    def test_documentation(self):
        self.assertTrue(len(Square.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Square.display.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Square.update.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/square.py',
                                     'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        self.assertIsInstance(self.s1, Square, "Not instance of Square")

    def test_subclass(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_id(self):
        """
        Testing id
        """
        self.assertEqual(self.s1.id, 11)
        self.assertEqual(self.s2.id, 1)
        self.assertEqual(self.s3.id, 2)

    def test_validation(self):
        """ Test attribute validation """
        with self.assertRaises(TypeError):
            self.s1.size = '5'
        with self.assertRaises(ValueError):
            self.s1.size = -4
        with self.assertRaises(TypeError):
            self.s2.size = 3.6
        with self.assertRaises(ValueError):
            self.s2.size = 0
        with self.assertRaises(TypeError):
            self.s3.x = [3, 4]
        with self.assertRaises(ValueError):
            self.s3.x = -1
        with self.assertRaises(TypeError):
            Square(4, 2, '0')
        with self.assertRaises(ValueError):
            Square(8, 4, -10)

    def test_less_excess_param(self):
        """ Test when 0 or 1 or more parameters passed """
        with self.assertRaises(TypeError):
            Square(3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            Square()

    def test_area(self):
        """ Tests area of Square """
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 16)
        self.assertEqual(self.s3.area(), 9)

    def test_display_1(self):
        """ Tests printing of square """
        s2d = "\n    ####\n    ####\n    ####\n    ####\n"
        f = io.StringIO()
        with redirect_stdout(f):
            self.s2.display()
        self.assertEqual(f.getvalue(), s2d)

    def test_display_2(self):
        """ Tests printing of square """
        s3d = "\n\n  ###\n  ###\n  ###\n"
        f = io.StringIO()
        with redirect_stdout(f):
            self.s3.display()
        self.assertEqual(f.getvalue(), s3d)

    def test_str(self):
        """ Tests __str__ return value """
        s1s = "[Square] (11) 5/2 - 10"
        s2s = "[Square] (1) 4/1 - 4"
        s3s = "[Square] (2) 2/2 - 3"
        self.assertEqual(str(self.s1), s1s)
        self.assertEqual(str(self.s2), s2s)
        self.assertEqual(str(self.s3), s3s)

    def test_update(self):
        """ Tests update of the arguments """
        self.s4 = Square(1, 2, 3, 4)
        s4s = "[Square] (4) 2/3 - 1"
        self.assertEqual(str(self.s4), s4s)
        self.s4.update(20)
        s4u1 = "[Square] (20) 2/3 - 1"
        self.assertEqual(str(self.s4), s4u1)
        self.s4.update(20, 30)
        s4u2 = "[Square] (20) 2/3 - 30"
        self.assertEqual(str(self.s4), s4u2)
        self.s4.update(15, 25, 35)
        s4u3 = "[Square] (15) 35/3 - 25"
        self.assertEqual(str(self.s4), s4u3)
        self.s4.update(10, 11, 12, 13)
        s4u4 = "[Square] (10) 12/13 - 11"
        self.assertEqual(str(self.s4), s4u4)

    def test_update2(self):
        """ Tests update of the arguments """
        self.s5 = Square(1, 1, 1)
        s5s = "[Square] (3) 1/1 - 1"
        self.assertEqual(str(self.s5), s5s)
        self.s5.update(x=3, size=10)
        s5u1 = "[Square] (3) 3/1 - 10"
        self.assertEqual(str(self.s5), s5u1)
        self.s5.update(14, 15, x=13, y=11)
        s5u2 = "[Square] (14) 3/1 - 15"
        self.assertEqual(str(self.s5), s5u2)
        self.s5.update(x=3, size=15, y=5, id=100)
        s5u3 = "[Square] (100) 3/5 - 15"
        self.assertEqual(str(self.s5), s5u3)
