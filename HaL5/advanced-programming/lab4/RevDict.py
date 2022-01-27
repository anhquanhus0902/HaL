#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    dct = dict()
    for i in range(1, n+1):
        dct[i] = int(str(i**2)[::-1])
    print(dct)
