#!/usr/bin/env python

import time
import traceback
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List

denominations4Evaluation = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
sOD = len(denominations4Evaluation)

def changeMoney(A: List[int], T: int) -> List[int]:
    A = sorted(A, reverse=True)
    n = len(A)
    k = [0 for i in range(n)]
    i = 0
    while i < n and T > 0:
        k[i] = int(T / A[i])
        T -= k[i]*A[i]
        i += 1
    if T > 0:
        k = [-1 for i in range(n)]
    return k
    
def generateRandomAmountMoney(numbersOfDigitOfAmountMoney: int) -> int:
    minMoney = 10**(numbersOfDigitOfAmountMoney-1)
    maxMoney = 10**numbersOfDigitOfAmountMoney - 1
    return random.randint(minMoney, maxMoney)
    
def calculateExecutionTime(randomT: int) -> int:
    startTime = time.time_ns()
    changeMoney(denominations4Evaluation, T)
    finishTime = time.time_ns()
    return finishTime-startTime
    
def evaluate(k: int) -> None:
    randomTs = executionTimes = np.array([])
    for i in range(1, k+1):
        randomT = generateRandomAmountMoney(i)
        randomTs = np.append(randomTs, randomT)
        executionTimes = np.append(executionTimes, calculateExecutionTime(randomT))
    plt.xlabel('Amount Money')
    plt.ylabel('Execution Time (nanosecond)')
    plt.plot(randomTs, executionTimes, marker='o')
    plt.show()

if __name__ == "__main__":
    try:
        print('Testing')
        T = int(input('Amount money: '))
        A = set()
        print('Denominations\n(press Enter to break)')
        denominationCounter = 1
        while True:
            denomination = input('Denomination #{}: '.format(denominationCounter))
            denominationCounter += 1
            if len(denomination) != 0:
                A.add(int(denomination))
            else:
                break
        A = list(A)
        res = changeMoney(A, T)
        print('Coins:', sorted(A, reverse=True))
        print(res)
        print('Numbers of coin: {}'.format(sum(res)))
        print('Evaluation')
        k = int(input('k = ?\n'))
        evaluate(k) if k > 0 else print('k > 0, plzz')
    except Exception:
        traceback.print_exc()
