#!/usr/bin/env python

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
