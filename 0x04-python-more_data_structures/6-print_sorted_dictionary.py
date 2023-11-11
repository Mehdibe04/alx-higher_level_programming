#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for llv in sorted(a_dictionary):
        print("{}: {}".format(llv, a_dictionary[llv]))
