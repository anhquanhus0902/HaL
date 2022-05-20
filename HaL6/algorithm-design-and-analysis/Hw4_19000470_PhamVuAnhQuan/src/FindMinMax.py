#!/usr/bin/env python

import time
import random
import traceback
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

def findMinMax(lst: List[int], l: int, r: int) -> Tuple[int, int]:
    if l == r:
        return (min(lst[l], lst[r]), max(lst[l], lst[r]))
    else:
        mid = (l+r)//2
        (min1, max1) = findMinMax(lst, l, mid)
        (min2, max2) = findMinMax(lst, mid+1, r)
        return (min(min1, min2), max(max1, max2))

def createRandomListOfIntegers(size: int) -> List[int]:
    a = [random.randint(-999, i+999) for i in range(size)]
    return a

def calculateExecutionTime(sizeOfList: int) -> int:
    a = createRandomListOfIntegers(sizeOfList)
    startTime = time.time_ns()
    findMinMax(a, 0, len(a)-1)
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
        print('Test')
        n = int(input('n = ?\n'))
        lst = createRandomListOfIntegers(n)
        print('Random list:\n{}'.format(lst))
        print(findMinMax(lst, 0, len(lst)-1))
        print('-----------------------------\nEvaluation')
        k = int(input('k = ?\n(pls choose a number that greater than or equal to 0 and smaller than 10 :))\n'))
        if (k >= 0):
            evaluate(k)
        else:
            print('k must be positive')
    except Exception:
        traceback.print_exc()
