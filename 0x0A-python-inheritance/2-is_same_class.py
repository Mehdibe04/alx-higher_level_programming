#!/usr/bin/python3
"""Defns a class-checkg func"""


def is_same_class(obj, a_class):
    """Check if an obj is exactly an instc of a gvn class

    Args:
         obj (any): d obj 2 check
         a_class (type): d class 2 match d type of obj 2
    Returns:
         If obj is exctly an instc of a_class then True
         False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
