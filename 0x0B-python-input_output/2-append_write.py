#!/usr/bin/python3
"""Module defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a str at d end of a txt f (UTF8)"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
