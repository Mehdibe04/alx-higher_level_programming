#!/usr/bin/python3
import sys


def slv_queen(N):
    def cn_place(pos, oc_pos):
        for x in range(len(oc_pos)):
            if oc_pos[x] == pos or \
                    oc_pos[x] - x == pos - len(oc_pos) or \
                    oc_pos[x] + x == pos + len(oc_pos):
                return False
        return True

    def plc_queen(oc_pos, tg_row, m):
        if tg_row == m:
            result.append(oc_pos)
            return
        for col in range(m):
            if cn_place(col, oc_pos):
                plc_queen(oc_pos + [col], tg_row + 1, m)

    result = []
    plc_queen([], 0, m)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    m = int(sys.argv[1])
    if m < 4:
        print("N must be at least 4")
        sys.exit(1)

    sol = slv_queen(m)
    for sl in sol:
        print([[x, sl[x]] for x in range(m)])
