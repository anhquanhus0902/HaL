#!/usr/bin/env python

import time
import random
import traceback
import matplotlib.pyplot as plt
from typing import List, Tuple

def getInput() -> Tuple[int, List[int]]:
    n = int(input('number of coins: '))
    coins = list()
    for i in range(n):
        coin = int(input('value of coin#{}: '.format(i+1)))
        coins.append(coin)
#     coins = [5,1,2,10,6,2]
#     n = len(coins)
    coins.insert(0, 0)
    return (n, coins)

def solve(n: int, coins: List[int]) -> int:
    F = [-190422 for i in range(n+1)]
    for i in range(n+1):
        if i == 0:
            F[i] = 0
        elif i == 1:
            F[i] = coins[i]
        else:
            F[i] = max(F[i-2]+coins[i], F[i-1])
    return max(F)

if __name__ == "__main__":
    try:
        n, coins = getInput()
        maxAmountOfMoney = solve(n, coins)
        print(maxAmountOfMoney)
    except Exception:
        traceback.print_exc()