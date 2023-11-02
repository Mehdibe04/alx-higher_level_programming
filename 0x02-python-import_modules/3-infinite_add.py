#!/usr/bin/python3

if __name__ == "__main__":
    """Infinite add all the args"""
    import sys

    ttl = 0
    for x in range(1, len(sys.argv)):
        ttl += int(sys.argv[x])
    print("{}".format(ttl))
