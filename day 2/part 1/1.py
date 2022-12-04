#!/usr/bin/env python3

S = {"X": 1, "Y": 2, "Z": 3}
WIN, DRAW, LOSS = 6, 3, 0
R = {
    "A": {"X": DRAW, "Y": WIN, "Z": LOSS},
    "B": {"X": LOSS, "Y": DRAW, "Z": WIN},
    "C": {"X": WIN, "Y": LOSS, "Z": DRAW},
}


def main():
    c = 0
    with open("input.txt", "r") as _fp:
        for row in [r.split() for r in _fp.readlines() if r]:
            shape, play = row
            print(shape, play, R[shape][play], S[play], " = ", R[shape][play] + S[play])
            c += R[shape][play] + S[play]
    print(c)


if __name__ == "__main__":
    main()
