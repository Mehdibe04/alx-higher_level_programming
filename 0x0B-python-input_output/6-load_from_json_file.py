#!/usr/bin/python3
"""load_from_jsonfile module"""
import json


def load_from_json_file(filename):
    """creates an Obj from a "JSON f" """
    with open(filename, 'r') as f:
        return json.load(f)
