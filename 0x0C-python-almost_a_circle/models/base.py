#!/usr/bin/python3
"""
This model contains the Base Class
"""
import json


class Base:
    """
    Declaring the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ - instantiation of Base Class
        Args:
            id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method for generating JSON string representation
        of  a list of dictionaries.
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns a list of JSON string
        representations
        Args:
            json_string: string representing a list of dicts
        """
        new_list = []
        if json_string is None or len(json_string) < 1:
            return new_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with attributes
        already set.
        Args:
            **dictionary: double pointer to dictionary
        """
        temp_instance = cls(6, 9)
        temp_instance.update(**dictionary)
        return temp_instance

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method to write JSON string representations
        to files
        Args:
            list_objs: a list of instances that inherit from Base
        """
        list_dicts = []
        for obj in list_objs:
                list_dicts.append(cls.to_dictionary(obj))
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            if list_dicts is None:
                f.write(list_dicts)
            else:
                f.write(json.dumps(list_dicts))

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances.
        Args:
            None
        """
        try:
            with open(cls.__name__+'.json', 'r', encoding='utf-8') as f:
                inst_list = cls.from_json_string(f.read())
            return [cls.create(**dic_pt) for dic_pt in inst_list]
        except IOError:
            return []
