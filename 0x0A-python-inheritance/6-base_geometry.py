#!/usr/bin/python3
"""
module for Geometry classes
"""


class BaseGeometry:
    """
    parent class for Geometry
    """
    def area(self):
        """
        calculates area
        """
        raise Exception('area() is not implemented')
