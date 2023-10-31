#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        rslt = 0
    else:
        rslt = 32
    print('{}'.format(chr(i - rslt)), end="")
