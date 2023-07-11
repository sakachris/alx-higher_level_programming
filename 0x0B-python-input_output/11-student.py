#!/usr/bin/python3
"""
module for class student
"""


class Student:
    """
    class student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        s_dict = {}
        if type(attrs) is list and (type(s) is str for s in attrs):
            for i in attrs:
                if i in self.__dict__:
                    s_dict[i] = self.__dict__[i]
            return s_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key in json:
            setattr(self, key, json[key])
