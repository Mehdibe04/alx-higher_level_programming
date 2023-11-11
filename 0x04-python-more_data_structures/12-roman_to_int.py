#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    romn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    intg = 0
    for x in range(len(roman_string)):
        if x > 0 and romn[roman_string[x]] > romn[roman_string[x - 1]]:
            intg += romn[roman_string[x]] - 2 * romn[roman_string[x - 1]]
        else:
            intg += romn[roman_string[x]]
    return (intg)
