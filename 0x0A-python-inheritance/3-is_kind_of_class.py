#!/usr/bin/python3
"""Defns a class & inhrtd class-checkg func"""


def is_kind_of_class(obj, a_class):
    """Check if an obj is an instnc or inhrtd instnc of a class

    Args:
        obj (any): d obj 2 check
        a_class (type): d class 2 match d type of obj 2
    Returns:
        If obj is an instnc or inhrtd instnc of a_class - True
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
