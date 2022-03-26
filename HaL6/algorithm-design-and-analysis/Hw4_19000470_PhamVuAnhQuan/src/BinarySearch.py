#!/usr/bin/env python

import time
import random
import traceback
import numpy as np
import matplotlib.pyplot as plt

def binarySearch(lst: list, target: int) -> int:
    n = len(lst)
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if lst[mid] < target:
            l = mid+1
        elif lst[mid] > target:
            r = mid-1
        else:
            return mid
    return -1

def createRandomListOfIntegers(size: int) -> list:
    a = [random.randint(-999, i+999) for i in range(size)]
    return a

def calculateExecutionTime(sizeOfList: int) -> int:
    a = sorted(createRandomListOfIntegers(sizeOfList))
    target = random.randint(-1499, 1499)
    startTime = time.time_ns()
    binarySearch(a, target)
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
        lst = sorted(createRandomListOfIntegers(n))
        print('Random list:\n{}'.format(lst))
        target = int(input('Pls choose the target number.\n'))
        print(binarySearch(lst, target))
        print('----------------------------Evaluation')
        k = int(input('k = ?\n(pls choose a number that greater than or equal to 0 and smaller than 10 :))\n'))
        if (k >= 0):
            evaluate(k)
        else:
            print('k must be positive')
    except Exception:
        traceback.print_exc()
