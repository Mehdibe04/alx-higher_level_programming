#!/usr/bin/python3
"""
    101-locked_class: class LockedClass
"""


class LockedClass:
    """
        A class that can  have ONLY one attribute first_name
        Attribute:
             first_name (str): name
    """
    __slots__ = ['first_name']
