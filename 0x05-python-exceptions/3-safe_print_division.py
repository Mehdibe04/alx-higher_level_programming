#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        rslt = a / b
        return rslt
    except ZeroDivisionError:
        rslt = None
        return rslt
    finally:
        print("Inside result: {}".format(rslt))
