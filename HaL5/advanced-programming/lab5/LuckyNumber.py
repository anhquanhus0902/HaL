#!/usr/bin/env python

import os

def isLuckyNumber(n):
    if n == 0:
        return False
    su = 0
    while (n > 0):
        su += n % 10
        n //= 10
    if su % 5 == 0:
        return True
    else:
        return False

def findLuckyNumber(fileName):
    f = open(fileName, "r")
    for line in f:
        line = line.rstrip()
        lst = line.split(" ")
        for s in lst:
            if s.isnumeric():
                n = int(s)
                if isLuckyNumber(n):
                    return n
    return 0

if __name__ == "__main__":
    path = "E:\\khac\\quan\\HaL\\HaL5\\AdvancedProgramming\\lab5\\testdir"
    os.chdir(path)
    fileName = "t1.txt"
    print(findLuckyNumber(fileName))
