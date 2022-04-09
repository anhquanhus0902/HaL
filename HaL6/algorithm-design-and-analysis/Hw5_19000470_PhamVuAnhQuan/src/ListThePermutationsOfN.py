#!/usr/bin/env python

import traceback
from typing import List

def solve(n: int) -> None:
    check = [False for i in range(n)]
    permutation = [0 for i in range(n)]
    solve1(n, check, permutation)

def solve1(n: int, check: List[bool], permutation: List[int], k: int = 0) -> None:
    for i in range(0, n):
        if check[i] == False:
            permutation[k] = i+1
            check[i] = True
            if k == n-1:
                print(permutation)
            else:
                solve1(n, check, permutation, k+1)
            check[i] = False


if __name__ == "__main__":
    try:
        n = int(input('n = ?\n'))
        solve(n) if n > 0 else print('n > 0, plz')
    except Exception:
        traceback.print_exc()
