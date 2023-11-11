#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    kys_2_delete = [k for k, val in a_dictionary.items() if val == value]
    for k in kys_2_delete:
        del a_dictionary[k]
    return a_dictionary
