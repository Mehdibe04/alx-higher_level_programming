#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    d = []
    for X in set_1:
        if X not in set_2:
            d.append(i)
    for X in set_2:
        if X not in set_1:
            d.append(X)
    return d
