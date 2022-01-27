#!/usr/bin/env python

def addNum(a, b):
    a = int(''.join(str(i) for i in a))
    b = int(''.join(str(i) for i in b))
    c = [int(i) for i in str(a+b)]
    return c


if __name__ == "__main__":
    a, b = list(), list()
    n, m = int(input()), int(input())
    for _ in range(n):
        a.append(int(input()))
    for _ in range(m):
        b.append(int(input()))
    print(addNum(a, b))
