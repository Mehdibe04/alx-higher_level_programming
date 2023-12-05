#!/usr/bin/python3
"""Dfns a clss Rect tht inhrts frm BsGmtry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rprsnt a rect usng BsGmtry."""

    def __init__(self, width, height):
        """Intlz a nw Rect

        Args:
            width (int): d wdth of d nw Rect
            height (int): d hght of d nw Rect
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
