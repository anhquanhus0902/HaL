#!/usr/bin/env python

from math import sqrt

def mean(lst):
    return sum(lst)/len(lst)

def variance(lst):
    e = mean(lst)
    n = len(lst)
    s = 0.0
    for i in range(n):
        s += (lst[i] - e)**2
    return s/n

def standarddeviation(lst):
    return sqrt(variance(lst))

if __name__ == "__main__":
    lst = list()
    n = int(input())
    for _ in range(n):
        inp = int(input())
        lst.append(inp)
