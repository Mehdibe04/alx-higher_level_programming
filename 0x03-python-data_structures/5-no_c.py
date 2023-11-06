#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for x in my_string:
        if x not in 'Cc':
            str += x
    return str
