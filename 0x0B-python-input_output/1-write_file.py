#!/usr/bin/python3
"""Module for write_file"""


def write_file(filename="", text=""):
    """write a str 2 a txt f (UTF8)"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
