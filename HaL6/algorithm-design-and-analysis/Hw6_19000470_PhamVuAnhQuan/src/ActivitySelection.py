#!/usr/bin/env python

import time
import random
import traceback
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

validActivity = lambda startTime, finishTime: finishTime >= startTime and startTime > 0

def activitySelector(activities: List[Tuple[int]]) -> List[Tuple[int]]:
    activities.sort(key=lambda actv:actv[1])
    S = [activities[0]]
    j = 0
    for i in range(1, len(activities)):
        if activities[i][0] >= activities[j][1]:
            S.append(activities[i])
            j = i
    return S

def generateRandomActivitiesSet(size: int) -> List[Tuple[int]]:
    randomActivitiesSet = set()
    se = size*5
    while len(randomActivitiesSet) < size:
        sTOA = random.randint(1, se)
        fTOA = random.randint(1, se)
        if validActivity(sTOA, fTOA):
            randomActivitiesSet.add((sTOA, fTOA))
    return list(randomActivitiesSet)

def calculateExecutionTime(activities: List[Tuple[int]]) -> int:
    startTime = time.time_ns()
    activitySelector(activities)
    finishTime = time.time_ns()
    return finishTime-startTime

def evaluate(k: int) -> None:
    numbersOfActvs = executionTimes = np.array([])
    for i in range(1, k+1):
        numbersOfActvs = np.append(numbersOfActvs, 10**i)
        executionTimes = np.append(executionTimes, calculateExecutionTime(generateRandomActivitiesSet(10**i)))
    plt.xlabel('Numbers of activity')
    plt.ylabel('Execution Time (nanosecond)')
    plt.plot(numbersOfActvs, executionTimes, marker='o')
    plt.show()

if __name__ == "__main__":
    try:
        print('Testing\nActivities\n(press Enter to break)')
        activitiesCounter = 1
        activities = set()
        while True:
            print('Activity #{}'.format(activitiesCounter))
            startTimeOfActivity = input('Start time: ')
            if len(startTimeOfActivity) == 0:
                break
            finishTimeOfActivity = input('Finish time: ')
            if len(finishTimeOfActivity) == 0:
                break
            startTimeOfActivity = int(startTimeOfActivity)
            finishTimeOfActivity = int(finishTimeOfActivity)
            if validActivity(startTimeOfActivity, finishTimeOfActivity):
                activities.add((startTimeOfActivity, finishTimeOfActivity))
                activitiesCounter += 1
            else:
                print('(not a valid activity. a valid activity: finish time > start time > 0)')
        activities = list(activities)
        print(activitySelector(activities)) if len(activities) != 0 else print('no activities')
        print('-------------------------\nEvaluation')
        k = int(input('k = ?\n'))
        evaluate(k) if k > 0 else print('k > 0, plzz')
    except Exception:
        traceback.print_exc()
