#!/usr/bin/env python

import os

def zeroMove(fileName):
    lst = []
    f = open(fileName , "r")
    for line in f:
        line = line.rstrip()
        lst = [int(i) for i in line.split(" ")]
    res = [i for i in lst if i != 0]
    for _ in range(len(lst)-len(res)):
        res.append(0)
    return res

if __name__ == "__main__":
    path = "E:\\khac\\quan\\HaL\\HaL5\\AdvancedProgramming\\lab5\\testdir"
    os.chdir(path)
    fileName = "t1.txt"
    print(zeroMove(fileName))
