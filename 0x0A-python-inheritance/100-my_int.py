#!/usr/bin/python3
"""
module contaning class that inherits int class
"""


class MyInt(int):
    """
    class inheriting class int
    """

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
