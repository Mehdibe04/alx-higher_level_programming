#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all the nm that are defined by bidden_4"""
    import hidden_4

    nm = dir(hidden_4)

    for x in nm:
        if x[:2] != "__":
            print(x)
