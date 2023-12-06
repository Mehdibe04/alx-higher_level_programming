#!/usr/bin/python3

"""Reads from standard input and computes metrics"""


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
    for status_c, cnt in sorted(status_cs.items()):
        if cnt > 0:
            print(f"{status_code}: {count}")

signal.signal(signal.SIGINT, signal_handler)

for ln in sys.stdin:
    prt = line.split()
    if len(prt) == 6:
        status_c = int(prt[3])
        if status_c in status_cs:
            status_cs[status_c] += 1
        total_s += int(prt[4])
        line_c += 1
        if line_c % 10 == 0:
            print_stats()
