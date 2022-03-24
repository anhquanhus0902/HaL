#!/usr/bin/env python

import time
import random
import traceback
import numpy as np
import matplotlib.pyplot as plt

def findMin(lst: list, l: int, r: int) -> int:
    if l == r:
        return lst[r]
    mid = (l+r)//2
    min1 = findMin(lst, l, mid)
    min2 = findMin(lst, mid+1, r)
    return min1 if min1<min2 else min2

def calculateExecutionTime(sizeOfArray: int) -> int:
    a = [random.randint(-999, i+999) for i in range(sizeOfArray)]
    startTime = time.time_ns()
    findMin(a, 0, len(a)-1)
    finishTime = time.time_ns()
    return finishTime-startTime

def evaluate(k: int) -> None:
    sizeOfArrays = executionTimes = np.array([])
    for i in range(k+1):
        sizeOfArrays = np.append(sizeOfArrays, 10**i)
        executionTimes = np.append(executionTimes, calculateExecutionTime(int(sizeOfArrays[i])))
    plt.xlabel('Input number')
    plt.ylabel('Execution Time (nanosecond)')
    plt.plot(sizeOfArrays, executionTimes, marker='o')
    plt.show()

if __name__ == "__main__":
    try:
        print('Evaluation')
        k = int(input('k = ?\n(pls choose a number that greater than or equal to 0 and smaller than 10 :))\n'))
        if (k >= 0):
            evaluate(k)
        else:
            print('k must be positive')
    except Exception:
        traceback.print_exc()
