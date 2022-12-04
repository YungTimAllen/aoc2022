#!/usr/bin/env python3
import string


PRIO = {l: p for p, l in enumerate(list(string.ascii_letters), start=1)}


def main():
    def check_collision(l1: str, l2: str, l3: str) -> str:
        for c in l1:
            if c in l2 and c in l3:
                return c

    with open("input.txt", "r") as _fp:
        rows = [r.strip() for r in _fp.readlines() if r]
        groups = [rows[n : n + 3] for n in range(0, len(rows), 3)]
        print(sum([PRIO[check_collision(*group)] for group in groups]))


if __name__ == "__main__":
    main()
