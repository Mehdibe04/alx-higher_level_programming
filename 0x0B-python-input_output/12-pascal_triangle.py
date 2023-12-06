#!/usr/bin/python3
""" Module that returns a list of lists of integers representing Pascal's"""


def pascal_triangle(n):
    """returns a list of lists of ints representg d Pascal's"""
    my_l = []
    for x in range(n):
        my_l.append([])
        for y in range(x+1):
            try:
                if y - 1 == -1:
                    my_l[x].append(1)
                else:
                    my_l[x].append(my_l[x-1][y-1] + my_l[x-1][y])
            except IndexError:
                my_l[x].append(1)
    return (my_l)
