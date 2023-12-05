#!/usr/bin/python3
"""Defns an inhrtd class-checkg func"""


def inherits_from(obj, a_class):
    """Checks if an obj is an inhrtd instnc of a class

    Args:
       obj (any): d obj 2 check
       a_class (type): d class 2 match d type of obj 2
    Returns:
       If obj is an inhrtd instnc of a_class - True
       False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
