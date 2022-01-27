#!/usr/bin/env python

def binary_to_decimal(n):
    return int(n, 2)

if __name__ == "__main__":
    lst = [i for i in input().split(",")]
    res = list()
    for i in lst:
        if binary_to_decimal(i) % 5 == 0:
            res.append(i)
    print(res)
