#!/usr/bin/env python

if __name__ == "__main__":
    a = int(input())
    res = 0
    for i in range(4):
        num = int(str(a) + str(a)*i)
        res += num
    print(res)
