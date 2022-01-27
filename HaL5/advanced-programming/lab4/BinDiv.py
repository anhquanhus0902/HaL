#!/usr/bin/env python

if __name__ == "__main__":
    lst = input().split(",")
    res = list()
    for i in lst:
        if int(i, 2) % 5 == 0:
            res.append(i)
    print(','.join(res))
