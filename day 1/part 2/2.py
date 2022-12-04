#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as _fp:
        cals = ",".join([l.strip() for l in _fp.readlines()]).split(",,")
        print(sum(sorted([sum([int(n) for n in m.split(",")]) for m in cals], reverse=True)[0:3]))


if __name__ == "__main__":
    main()
