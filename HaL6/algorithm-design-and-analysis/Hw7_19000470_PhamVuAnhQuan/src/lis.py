#!/usr/bin/env python

import time
import random
import traceback
import matplotlib.pyplot as plt
from typing import List, Tuple

def getInput() -> List[int]:
    a = input('enter the elements of the sequence (separate by SPACE): ')
    a = [int(el) for el in a.split()]
    #a = [2,5,4,6,3,8,9,7]
    a.insert(0, 999999999999999999999999999)
    return a
    
def L(i: int, a: List[int]) -> int:
    if i == 0 or i == 1:
        return i
    else:
        maxi = 1
        for j in range(1, i):
            if a[j] < a[i]:
                maxi = max(maxi, L(j, a)+1)
        return maxi

def solve(a: List[int]) -> Tuple[int, List[int]]:
    tbl = [-180422 for i in range(len(a))]
    for i in range(len(a)):
        tbl[i] = L(i, a)
    longest = max(tbl)
    # trace
    i = tbl.index(longest)
    subseq = [a[i]]
    longestCp = longest
    for j in range(i, 0, -1):
        if a[j] < a[i] and tbl[j] == longestCp-1:
            subseq.insert(0, a[j])
            longestCp -= 1
    return longest, subseq
    
def executionTime(a: List[int]) -> int:
    # nanosec
    executionTime = []
    for i in range(50):
        startTime = time.time_ns()
        solve(a)
        finishTime = time.time_ns()
        executionTime.append(finishTime-startTime)
    return int(sum(executionTime)/len(executionTime))
    
def generateRandomSequence(lenOfSeq: int) -> List[int]:
    a = [random.randint(0, lenOfSeq*10-1) for i in range(lenOfSeq)]
    a.insert(0, 999999999999999999999999999)
    return a
    
def evaluate(k: int) -> None:
    lenOfSeqs = [10*i for i in range(1, k+1)]
    executionTimes = list()
    for i in range(k):
        randomSeq = generateRandomSequence(lenOfSeqs[i])
        executionTimes.append(executionTime(randomSeq))
    plt.xlabel('Length of the sequence')
    plt.ylabel('Execution time (second)')
    plt.plot(lenOfSeqs, executionTimes, marker='o')
    plt.show()

if __name__ == "__main__":
    try:
        a = getInput()
        longest, subseq = solve(a)
        print('Longest:', longest)
        print(subseq)
        if input('Evaluate? (Y/n) ').lower() == 'y':
            evaluate(7)
        else:
            print('bye')
    except Exception:
        traceback.print_exc()