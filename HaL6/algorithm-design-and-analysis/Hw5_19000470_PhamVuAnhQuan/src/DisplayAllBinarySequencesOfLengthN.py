#!/usr/bin/env python

import traceback

def listToString(lst: list, separator: str = ' ') -> str:
    return separator.join(str(el) for el in lst)

def solve1(n: int) -> None:
    x = [290322 for i in range(n)]
    solve(x, n)

def solve(x: list, n: int, i: int = 0) -> None:
    for v in range(2):
        x[i] = v
        if i == n-1:
            print(listToString(x, ''))
        else:
            solve(x, n, i+1)

if __name__ == "__main__":
    try:
        n = int(input('Enter the length n: '))
        if n > 0:
            solve1(n)
        else:
            print('n > 0, plz')
    except Exception:
        traceback.print_exc()
