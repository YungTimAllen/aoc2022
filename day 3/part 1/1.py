#!/usr/bin/env python3
import string


PRIO = {l: p for p, l in enumerate(list(string.ascii_letters), start=1)}


def main():
    def check_collision(l1: str, l2: str) -> str:
        for c in l1:
            if c in l2:
                return c

    s = 0
    with open("input.txt", "r") as _fp:
        for row in [r.strip() for r in _fp.readlines() if r]:
            first, second = row[: len(row) // 2], row[len(row) // 2 :]
            s += PRIO[check_collision(first, second)]

    print(s)


if __name__ == "__main__":
    main()
