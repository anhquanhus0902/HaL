#!/usr/bin/env python

if __name__ == "__main__":
    amt = 0
    while True:
        line = input()
        if len(line) == 0:
            break
        if line[0] == 'D':
            amt += int(line[2:])
        elif line[0] == 'W':
            amt -= int(line[2:])
    print(amt)
