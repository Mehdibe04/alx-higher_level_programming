#!/usr/bin/python3
"""Dfns a class Rect tht inhrts from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rprsnt a rect usng BaseGeometry"""

    def __init__(self, width, height):
        """Intlz a nw Rect

        Args:
            width (int): d wdth of d nw Rect
            height (int): d hght of d nw Rect
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of d rect"""
        return self.__width * self.__height

    def __str__(self):
        """Return d prnt() and str() rprsntt of a Rect"""
        strg = "[" + str(self.__class__.__name__) + "] "
        strg += str(self.__width) + "/" + str(self.__height)
        return strg
