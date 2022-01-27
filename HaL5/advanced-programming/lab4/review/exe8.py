#!/usr/bin/env python

from operator import itemgetter

if __name__ == "__main__":
    lst = []
    while True:
        line = input()
        if len(line) == 0:
            break
        info = tuple(line.split(","))        
        lst.append(info)
    sorted_lst = sorted(lst, key = itemgetter(0, 1, 2))
    print(sorted_lst)
