#!/usr/bin/python3
"""Defines an obj attrbt lkup func"""


def lookup(obj):
    """Return a lst of an obj's available attrbts"""
    return (dir(obj))
