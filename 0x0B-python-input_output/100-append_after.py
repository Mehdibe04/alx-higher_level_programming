#!/usr/bin/python3
"""Module for append_after method"""


def append_after(filename="", search_string="", new_string=""):
    """Append a ln of txt 2 a f after
     each ln containg a spcfc str"""
    new_ctt = ""
    with open(filename, "r") as f:
        for ln in f:
            new_ctt += ln
            if search_string in ln:
                new_ctt += new_string
    with open(filename, "w") as f:
        f.write(new_ctt)
