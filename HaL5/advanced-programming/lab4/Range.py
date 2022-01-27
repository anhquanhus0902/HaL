#!/usr/bin/env python

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    while a <= b:
        if a % 11 == 0:
            if a % 3 != 0:
                print(a, end="; ")
            a += 11
        else:
            a += 1
