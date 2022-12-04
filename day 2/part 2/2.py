#!/usr/bin/env python3

S = {"A": 1, "B": 2, "C": 3, "Z": 6, "Y": 3, "X": 0}

R = {
    "A": {"X": "C", "Y": "A", "Z": "B"},
    "B": {"X": "A", "Y": "B", "Z": "C"},
    "C": {"X": "B", "Y": "C", "Z": "A"},
}


def main():
    c = 0
    with open("input.txt", "r") as _fp:
        for row in [r.split() for r in _fp.readlines() if r]:
            shape, outcome = row
            c += S[R[shape][outcome]] + S[outcome]
    print(c)


if __name__ == "__main__":
    main()
