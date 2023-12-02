#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Prints txt with 2 new lines after each '.', '?', and ':'.

    Args:
        text (string): txt to be printed
    Raises:
        TypeError: If txt is not a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    z = 0
    while z < len(text) and text[z] == ' ':
        z += 1

    while z < len(text):
        print(text[z], end="")
        if text[z] == "\n" or text[z] in ".?:":
            if text[z] in ".?:":
                print("\n")
            z += 1
            while z < len(text) and text[z] == ' ':
                z += 1
            continue
        z += 1
