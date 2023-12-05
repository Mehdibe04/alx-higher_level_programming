#!/usr/bin/python3
"""Dfns a funct tht adds attrbts 2 obj"""


def add_attribute(obj, att, value):
    """Add a nw attrbt 2 an obj if pssbl

    Args:
         obj (any): d obj 2 add an attrbt 2
         att (str): d nm of d attrbt 2 add 2 obj
         value (any): d val of att
    Raises:
        TypeError: If d attrbt cnnt be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
