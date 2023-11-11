#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    d = []
    for i in set_1:
        if i not in set_2:
            d.append(i)
    for j in set_2:
        if j not in set_1:
            d.append(j)
    return d
