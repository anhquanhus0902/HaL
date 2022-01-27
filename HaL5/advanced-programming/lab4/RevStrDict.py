#!/usr/bin/env python

if __name__ == "__main__":
    lst = input().split()
    dct = dict()
    for s in lst:
        dct[s] = s + s[::-1]
    print(dct)
    
