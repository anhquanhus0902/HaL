#!/usr/bin/env python

if __name__ == "__main__":
    for i in range(1100, 9091):
        if i % 11 == 0 and i % 3 != 0:
            print(i, end="; ")
