#!/usr/bin/python3
"""Dfns a bs gmtry clss BaseGmtry"""


class BaseGeometry:
    """Rprsnt bs gmtry"""

    def area(self):
        """Not yet implmntd"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Vldt a param as an int

        Args:
            name (str): d name of d param
            value (int): d param 2 vldt
        Raises:
            TypeError: If val is nt an int
            ValueError: If val is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
