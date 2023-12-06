#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """returns d dictio dscrption wth simple data struct
    (list, dictio, str, int & boolean) for JSON serialztion"""

    return obj.__dict__
