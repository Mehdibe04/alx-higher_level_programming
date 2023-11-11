#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    Nw_dc = {}
    for x in a_dictionary:
        Nwval = (a_dictionary.get(x)) * 2
        Nw_dc.update({x: Nwval})
    return (Nw_dc)
