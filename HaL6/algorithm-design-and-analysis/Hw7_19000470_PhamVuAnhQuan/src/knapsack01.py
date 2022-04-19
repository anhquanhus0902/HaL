#!/usr/bin/env python

import time
import random
import traceback
import matplotlib.pyplot as plt
from typing import List, Tuple

def getInput() -> Tuple[int, List[Tuple[int]]]:
    n = int(input('number of items: '))
    bp = list()
    for i in range(n):
        p = int(input('value of item #{}: '.format(i+1)))
        w = int(input('weight of item #{}: '.format(i+1)))
        bp.append((p,w))
#     n = 4
#     bp = [(3,2),(2,1),(2,2),(1,1)]
    bp.insert(0, (0,0))
    return (n, bp)

def C(i: int, j: int, bp: List[Tuple[int]]) -> int:
    if i == 0 or j == 0:
        return 0
    elif bp[i][1] > j:
        return C(i-1, j, bp)
    else:
        return max(C(i-1, j, bp), C(i-1, j-bp[i][1], bp)+bp[i][0])

def solve(n: int, bp: List[Tuple[int]]) -> Tuple[int, List[Tuple[int]]]:
    tbl = dict()
    for i in range(n+1):
        for j in range(n+1):
            tbl[(i,j)] = C(i, j, bp)
    # trace
    CMax = max(tbl, key=tbl.get)
    maxValue = tbl[CMax]
    resBp = list()
    i, j = CMax
    while i > 0 and j > 0:
        if tbl[(i,j)] == tbl[(i-1,j)]:
            i -= 1
        elif tbl[(i,j)] == tbl[(i-1,j-bp[i][1])] + bp[i][0]:
            resBp.insert(0, bp[i])
            j -= bp[i][1]
            i -= 1      
    return maxValue, resBp
    
def executionTime(n: int, bp: List[Tuple[int]]) -> int:
    executionTime = list()
    for i in range(50):
        startTime = time.time_ns()
        solve(n, bp)
        finishTime = time.time_ns()
        executionTime.append(finishTime-startTime)
    return int(sum(executionTime)/len(executionTime))

def generateRandomBp(n: int) -> List[Tuple[int]]:
    randomBp = [(random.randint(1, 10000), random.randint(1, 10000)) for i in range(n)]
    randomBp.insert(0, (0,0))
    return randomBp

def evaluate(k: int) -> None:
    numberOfItems = [10*i for i in range(1, k+1)]
    executionTimes = list()
    for i in range(k):
        executionTimes.append(executionTime(numberOfItems[i], generateRandomBp(numberOfItems[i])))
    plt.xlabel('Number of times')
    plt.ylabel('Execution time (nanosec)')
    plt.plot(numberOfItems, executionTimes, marker='o')
    plt.show()
        
if __name__ == "__main__":
    try:
        n, bp = getInput()
        maxValue, resBp = solve(n, bp)
        print('max value:', maxValue)
        print(resBp)
        if input('Evaluate? (Y/n) ').lower() == 'y':
            evaluate(7)
        else:
            print('bye')
    except Exception:
        traceback.print_exc()