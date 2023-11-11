#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        x = list(a_dictionary.values())
        y = list(a_dictionary.keys())
        return (y[x.index(max(x))])
