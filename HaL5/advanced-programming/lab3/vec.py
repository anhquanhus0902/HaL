#!/usr/bin/env python

from math import sqrt

def cosineb2v(u, v):
    s, u_, v_ = 0, 0, 0
    for i in range(len(u)):
        s += u[i]*v[i]
        u_ += u[i]**2
        v_ += v[i]**2
    u_ = sqrt(u_)
    v_ = sqrt(v_)
    return s/(u_*v_)

if __name__ == "__main__":
    n = int(input())
    u = list()
    v = list()
    for _ in range(n):
        u.append(int(input()))
    for _ in range(n):
        v.append(int(input()))
    print(cosineb2v(u, v))
