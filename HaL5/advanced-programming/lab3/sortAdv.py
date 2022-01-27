#!/usr/bin/env python

def customSort(lst):
    even_lst, odd_lst = list(), list()
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    even_lst.sort()
    odd_lst.sort(reverse=True)
    lst = even_lst + odd_lst
    return lst

if __name__ == "__main__":
    lst = list()
    n = int(input())
    for _ in range(n):
        inp = int(input())
        lst.append(inp)
    lst = customSort(lst)
    print(lst)
