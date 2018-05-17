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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public instance method that retrieves a dictionary
        representation of a Student instance.
        """
        at = attrs
        if not isinstance(at, list):
            return self.__dict__
        for item in at:
            if not isinstance(item, str):
                return self.__dict__
        if at:
            return {k: v for (k, v) in self.__dict__.items() if k in at}
        return self.__dict__
