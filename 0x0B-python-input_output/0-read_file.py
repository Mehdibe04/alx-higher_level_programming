#!/usr/bin/python3
"""Module for read_file"""


def read_file(file=""):
    """Reads a txt f (UTF8) and prnts it 2 stdout"""
    with open(file, encoding="utf-8") as f:
        print(f.read(), end="")
