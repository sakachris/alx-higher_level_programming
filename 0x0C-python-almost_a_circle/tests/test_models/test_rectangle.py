#!/usr/bin/python3
"""
test_models/rectangle.py for testing Rectangle class
"""
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
import pycodestyle


class TestBase(unittest.TestCase):
    """
    Testing for Base Class
    """
    def setUp(self):
        self.r1 = Rectangle(10, 5, 2, 1)
        self.r2 = Rectangle(4, 4, 1, 4, 9)
        self.r3 = Rectangle(3, 2, 1, 1)

    def test_documentation(self):
        self.assertTrue(len(Rectangle.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.area.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.display.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/rectangle.py',
                                     'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        self.assertIsInstance(self.r1, Rectangle, "Not instance of Rectangle")

    def test_id(self):
        """
        Testing id
        """
        self.assertEqual(self.r1.id, 16)
        self.assertEqual(self.r2.id, 9)
        self.assertEqual(self.r3.id, 17)

    def test_validation(self):
        """ Test attribute validation """
        with self.assertRaises(TypeError):
            self.r1.width = '5'
        with self.assertRaises(ValueError):
            self.r1.width = -4
        with self.assertRaises(TypeError):
            self.r2.height = 3.6
        with self.assertRaises(ValueError):
            self.r2.height = 0
        with self.assertRaises(TypeError):
            self.r3.x = [3, 4]
        with self.assertRaises(ValueError):
            self.r3.x = -1
        with self.assertRaises(TypeError):
            Rectangle(4, 2, 0, '0')
        with self.assertRaises(ValueError):
            Rectangle(8, 4, 0, -10)

    def test_area(self):
        """ Tests area of Rectangle """
        self.assertEqual(self.r1.area(), 50)
        self.assertEqual(self.r2.area(), 16)
        self.assertEqual(self.r3.area(), 6)

    def test_display_1(self):
        """ Tests printing of rectangle """
        r2d = "####\n####\n####\n####\n"
        f = io.StringIO()
        with redirect_stdout(f):
            self.r2.display()
        self.assertEqual(f.getvalue(), r2d)

    def test_display_2(self):
        """ Tests printing of rectangle """
        r3d = "###\n###\n"
        f = io.StringIO()
        with redirect_stdout(f):
            self.r3.display()
        self.assertEqual(f.getvalue(), r3d)
