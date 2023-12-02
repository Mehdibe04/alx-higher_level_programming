#!/usr/bin/python3
"""
Defines a matrix div func
"""

def matrix_divided(matrix, div):
    """Divide all elmts of a matrx

    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): The div
    Raises:
        TypeError: If the matrx contains non-nums
    Returns:
        A new matrx representg the res of the div
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    m_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(m_type)

    l_e = 0
    m_size = "Each row of the matrix must have the same size"

    for ele in matrix:
        if not ele or not isinstance(ele, list):
            raise TypeError(m_type)

        if l_e != 0 and len(ele) != l_e:
            raise TypeError(m_size)

        for num in ele:
            if not type(num) in (int, float):
                raise TypeError(m_type)

        l_e = len(ele)

    g = list(map(lambda i: list(map(lambda j: round(j / div, 2), i)), matrix))
    return (g)
