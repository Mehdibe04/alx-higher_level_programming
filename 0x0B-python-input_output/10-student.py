#!/usr/bin/python3
"""class Student that defines a student by:"""


class Student:
    """class Student that defines a student by:"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation"""
        if att is None:
            return self.__dict__
        else:
            my_dictio = {}
            for x in att:
                if hasattr(self, x):
                    my_dictio[x] = getattr(self, x)
            return my_dictio
