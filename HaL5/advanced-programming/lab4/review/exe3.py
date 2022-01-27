#!/usr/bin/env python

if __name__ == "__main__":
    dct = dict()
    s = input().split(" ")
    for i in s:
        dct[i] = i + i[::-1]
    print(dct)
