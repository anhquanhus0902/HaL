#!/usr/bin/env python

def length(t):
    res = 1
    for i in range(len(t)-1):
        if t[i] != t[i+1]:
            res += 1
    return res*2
    
def compress(t):
    res = []
    count = 1
    if t[-1] == 0:
        t.append(1)
    else:
        t.append(0)
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            count += 1
        else:
            res.append(t[i])
            res.append(count)
            count = 1
    return res
    
def lengthInverse(ct):
    res = 0
    for i in range(len(ct)):
        if i % 2 == 0:
            continue
        res += ct[i]
    return res
    
def decompress(ct):
    res = []
    for i in range(len(ct)):
        if i % 2 == 0:
            continue
        for j in range(ct[i]):
            res.append(ct[i-1])
    return res

if __name__ == "__main__":
    t = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    print(length(t))
    print(compress(t))
    print(lengthInverse([0,5,1,1,0,5]))
    print(decompress([0,5,1,1,0,5]))