#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number and list of arguments"""
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for x in range(len(sys.argv) - 1):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
