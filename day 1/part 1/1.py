#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as _fp:
        cal_per_elf = ",".join([l.strip() for l in _fp.readlines()]).split(",,")
        print(max([sum([int(n) for n in m.split(",")]) for m in cal_per_elf]))


if __name__ == "__main__":
    main()
