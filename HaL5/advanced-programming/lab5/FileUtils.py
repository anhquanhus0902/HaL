#!/usr/bin/env python

import os
from operator import itemgetter

def searchInFiles(x, path):
    lst = list()
    files = os.listdir(path)
    for file in files:
        f = open(file, "r")
        for line in f:
            if x in line:
                st = (file, line)
                lst.append(st)
                break
        lst = sorted(lst, key = itemgetter(0))
    return lst

if __name__ == "__main__":
    path = "E:\\khac\\quan\\HaL\\HaL5\\AdvancedProgramming\\lab5\\testdir"
    x = "haha"
    os.chdir(path)
    print(searchInFiles(x, path))
