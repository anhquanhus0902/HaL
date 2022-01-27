#!/usr/bin/env python

if __name__ == "__main__":
    amount = 0
    f = open("test.txt", "r")
    for line in f:
        trans = line.rstrip().split(" ")
        if trans[0] == 'D':
            amount += int(trans[1])
        elif trans[0] == 'W':
            amount -= int(trans[1])
    print(amount)
