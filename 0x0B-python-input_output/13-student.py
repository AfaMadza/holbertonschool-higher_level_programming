#!/usr/bin/python3
"""
This module contains the definition of the Class Student
"""


class Student:
    """
    Student - see module description
    Args:
        None
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__ - instantiation of the Student Class
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance.
        """
        at = attrs
        if at:
            return {k: v for (k, v) in self.__dict__.items() if k in at}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of
        of the Student instance.
        """
        for k, v in json.items():
            setattr(self, k, v)
