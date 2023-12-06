#!/usr/bin/python3
"""Module that creates an Object from a "JSON file" """
import json


def save_to_json_file(my_obj, filename):
    """save 2 json f"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
