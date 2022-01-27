#!/usr/bin/env python

from math import sqrt

def solve(paths):
    x = y = 0
    for path in paths:
        if path[0] == 'UP':
            y += int(path[1])
        elif path[0] == 'DOWN':
            y -= int(path[1])
        elif path[0] == 'LEFT':
            x -= int(path[1])
        elif path[0] == 'RIGHT':
            x += int(path[1])
    res = sqrt(x**2 + y**2)
    print(int(res))

if __name__ == "__main__":
    paths = []
    while True:
        line = input()
        if len(line) == 0:
            break
        path = tuple(line.split(" "))
        paths.append(path)
    solve(paths)
