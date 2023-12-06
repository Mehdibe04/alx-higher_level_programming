#!/usr/bin/python3

"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys
import signal

total_s = 0
status_cs = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_c = 0

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print(f"Total file size: {total_size}")
    for status_cod, ct in sorted(status_cs.items()):
        if ct > 0:
            print(f"{status_code}: {count}")

signal.signal(signal.SIGINT, signal_handler)

for ln in sys.stdin:
    prts = ln.split()
    if len(prts) == 6:
        status_cod = int(prts[3])
        if status_cod in status_cs:
            status_cs[status_cod] += 1
        total_s += int(prts[4])
        line_c += 1
        if line_c % 10 == 0:
            print_stats()
