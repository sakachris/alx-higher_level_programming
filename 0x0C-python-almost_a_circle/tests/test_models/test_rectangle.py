#!/usr/bin/python3
"""
test_models/rectangle.py for testing Rectangle class
"""
import unittest
import io
import os
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class TestBase(unittest.TestCase):
    """
    Testing for Base Class
    """
    def setUp(self):
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 5, 2, 1)
        self.r2 = Rectangle(4, 4, 1, 4, 9)
        self.r3 = Rectangle(3, 2, 2, 1)

    def test_documentation(self):
        self.assertTrue(len(Rectangle.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.area.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.display.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.update.__doc__) >= 20, "Short doc")
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 20, "Short")
        self.assertTrue(len(Rectangle.to_json_string.__doc__) >= 20, "Short")

    def test_pycodestyle(self):
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/rectangle.py',
                                     'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        self.assertIsInstance(self.r1, Rectangle, "Not instance of Rectangle")

    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id(self):
        """
        Testing id
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 9)
        self.assertEqual(self.r3.id, 2)

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

    def test_validation2(self):
        """ Test attribute validation """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(4, -7)
        with self.assertRaises(ValueError):
            Rectangle(-3, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 8)
        with self.assertRaises(ValueError):
            Rectangle(4, 0)
        with self.assertRaises(ValueError):
            Rectangle(8, 4, -7)

    def test_less_excess_param(self):
        """ Test when 0 or 1 or excess parameters passed """
        with self.assertRaises(TypeError):
            Rectangle(3)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_area(self):
        """ Tests area of Rectangle """
        self.assertEqual(self.r1.area(), 50)
        self.assertEqual(self.r2.area(), 16)
        self.assertEqual(self.r3.area(), 6)

    def test_display_1(self):
        """ Tests printing of rectangle """
        r2d = "\n\n\n\n ####\n ####\n ####\n ####\n"
        f = io.StringIO()
        with redirect_stdout(f):
            self.r2.display()
        self.assertEqual(f.getvalue(), r2d)

    def test_display_2(self):
        """ Tests printing of rectangle """
        r3d = "\n  ###\n  ###\n"
        f = io.StringIO()
        with redirect_stdout(f):
            self.r3.display()
        self.assertEqual(f.getvalue(), r3d)

    def test_display_3(self):
        """ Tests printing of rectangle """
        r7 = Rectangle(4, 4)
        r7d = "####\n####\n####\n####\n"
        f = io.StringIO()
        with redirect_stdout(f):
            r7.display()
        self.assertEqual(f.getvalue(), r7d)

    def test_display_4(self):
        """ Tests printing of rectangle """
        r8 = Rectangle(3, 2)
        r8d = "###\n###\n"
        f = io.StringIO()
        with redirect_stdout(f):
            r8.display()
        self.assertEqual(f.getvalue(), r8d)

    def test_str(self):
        """ Tests __str__ return value """
        r1s = "[Rectangle] (1) 2/1 - 10/5"
        r2s = "[Rectangle] (9) 1/4 - 4/4"
        r3s = "[Rectangle] (2) 2/1 - 3/2"
        self.assertEqual(str(self.r1), r1s)
        self.assertEqual(str(self.r2), r2s)
        self.assertEqual(str(self.r3), r3s)

    def test_update(self):
        """ Tests update of the arguments """
        self.r4 = Rectangle(1, 2, 3, 4)
        r4s = "[Rectangle] (3) 3/4 - 1/2"
        self.assertEqual(str(self.r4), r4s)
        self.r4.update(20)
        r4u1 = "[Rectangle] (20) 3/4 - 1/2"
        self.assertEqual(str(self.r4), r4u1)
        self.r4.update(20, 30)
        r4u2 = "[Rectangle] (20) 3/4 - 30/2"
        self.assertEqual(str(self.r4), r4u2)
        self.r4.update(15, 25, 35)
        r4u3 = "[Rectangle] (15) 3/4 - 25/35"
        self.assertEqual(str(self.r4), r4u3)
        self.r4.update(10, 11, 12, 13)
        r4u4 = "[Rectangle] (10) 13/4 - 11/12"
        self.assertEqual(str(self.r4), r4u4)
        self.r4.update(5, 10, 15, 20, 25)
        r4u5 = "[Rectangle] (5) 20/25 - 10/15"
        self.assertEqual(str(self.r4), r4u5)

    def test_update2(self):
        """ Tests update of the arguments """
        self.r5 = Rectangle(1, 1, 1, 1)
        r5s = "[Rectangle] (3) 1/1 - 1/1"
        self.assertEqual(str(self.r5), r5s)
        self.r5.update(x=3, height=10)
        r5u1 = "[Rectangle] (3) 3/1 - 1/10"
        self.assertEqual(str(self.r5), r5u1)
        self.r5.update(14, 15, x=13, height=11)
        r5u2 = "[Rectangle] (14) 3/1 - 15/10"
        self.assertEqual(str(self.r5), r5u2)
        self.r5.update(x=3, height=15, y=5, id=100, width=20)
        r5u3 = "[Rectangle] (100) 3/5 - 20/15"
        self.assertEqual(str(self.r5), r5u3)

    def test_to_dictionary(self):
        """ Tests dictionary of instances """
        r1d = {'width': 10, 'height': 5, 'x': 2, 'y': 1, 'id': 1}
        self.assertDictEqual(self.r1.to_dictionary(), r1d)
        r2d = {'width': 4, 'height': 4, 'x': 1, 'y': 4, 'id': 9}
        self.assertDictEqual(self.r2.to_dictionary(), r2d)
        self.r6 = Rectangle(30, 40)
        r6d = {'width': 30, 'height': 40, 'x': 0, 'y': 0, 'id': 3}
        self.assertDictEqual(self.r6.to_dictionary(), r6d)

    def test_to_json_string(self):
        """ Tests conversion of dict to list of json string """
        r1j = '[{"width": 10, "height": 5, "x": 2, "y": 1, "id": 1}]'
        js = Base.to_json_string([self.r1.to_dictionary()])
        self.assertEqual(js, r1j)
        self.assertIsInstance(js, str)

    def test_save_to_file(self):
        """ Tests saving to json file """
        Rectangle.save_to_file([self.r1, self.r2])
        self.assertTrue(os.path.isfile('Rectangle.json'))

    def test_save_to_file_2(self):
        """ Tests saving to json file """
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile('Rectangle.json'))
        with open('Rectangle.json') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_3(self):
        """ Tests saving to json file """
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.isfile('Rectangle.json'))
        r = '[{"width": 1, "height": 2, "x": 0, "y": 0, "id": 3}]'
        with open('Rectangle.json') as file:
            self.assertEqual(file.read(), r)

    def test_load_from_file(self):
        output = Rectangle.load_from_file()
        for out in output:
            self.assertEqual(str(out), '[Rectangle] (3) 0/0 - 1/2')

    def test_create_1(self):
        r = Rectangle.create(**{'id': 89})
        rs = '[Rectangle] (89) 0/0 - 1/1'
        self.assertEqual(str(r), rs)

    def test_create_2(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        rs = '[Rectangle] (89) 0/0 - 1/2'
        self.assertEqual(str(r), rs)

    def test_create_3(self):
        r = Rectangle.create(**{'id': 89, 'width': 1,
                             'height': 2, 'x': 3, 'y': 4})
        rs = '[Rectangle] (89) 3/4 - 1/2'
        self.assertEqual(str(r), rs)
