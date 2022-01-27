#!/usr/bin/env python

import os

def findCouple(fileName):
    f = open(fileName, "r")
    for line in f:
        lst = line.rstrip().split(" ")
        for i in range(len(lst)-1):
            for j in range(i+1, len(lst)):
                if lst[j] == (lst[i])[::-1]:
                    return (lst[i], lst[j])
    return ("None", "None")

if __name__ == "__main__":
    path = "E:\\khac\\quan\\HaL\\HaL5\\AdvancedProgramming\\lab5\\testdir"
    os.chdir(path)
    fileName = "t1.txt"
    print(findCouple(fileName))
