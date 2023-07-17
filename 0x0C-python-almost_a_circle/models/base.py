#!/usr/bin/python3
"""
base module for the Base class
"""
import json


class Base:
    """
    class Base for all classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string to a file """
        filename = f"{cls.__name__}.json"
        dict_list = []
        if list_objs is not None:
            for objs in list_objs:
                dict_list.append(objs.to_dictionary())
        with open(filename, mode='w', encoding='UTF-8') as file:
            file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """  returns the list of the JSON string representation """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, encoding='UTF-8') as file:
                dict_list = cls.from_json_string(file.read())
        except IOError:
            return []
        instances = []
        for dct in dict_list:
            instances.append(cls.create(**dct))
        return instances
