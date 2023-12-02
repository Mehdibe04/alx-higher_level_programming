#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Prints a square wid d # char

    Args:
        size (int): The height/width of d square
    Raises:
        TypeError: If sz is not an int
        ValueError: If sz is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
