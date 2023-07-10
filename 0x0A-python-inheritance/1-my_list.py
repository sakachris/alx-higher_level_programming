#!/usr/bin/python3
"""
module contaning class that inherits list
"""


class MyList(list):
    """
    class inheriting class list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
