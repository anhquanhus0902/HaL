#!/usr/bin/env python

# @student: Pham Vu Anh Quan
# @id:      19000470
# @module:  MAT2411E - Optimization 2022sem2

import time
from math import *
import numpy as np

# Rosembrock function: f(x) = 100(x_2 - x_1**2)**2 + (1 - x_1)**2
# Global minimum of this function lies at the point (1,1)
Rosembrock = lambda x: 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

firstOrderGradientOfRosembrock = lambda x: np.array([400*x[0]**3 - 400*x[0]*x[1] + 2*x[0] - 2, 200*(x[1]-x[0]**2)])

secondOrderGradientOfRosembrock = lambda x: np.array([[1200*x[0]**2 - 400*x[1] + 2, -400*x[0]], [-400*x[0], 200]])

stopCondition = lambda x: sqrt(firstOrderGradientOfRosembrock(x)[0]**2  + firstOrderGradientOfRosembrock(x)[1]**2) <= 10**-4

startPoints = [np.array([1.2, 1.2]), np.array([-1.2, 1])]
actualResult = np.array([1, 1])

stopReasons = (
    'Stop reason: norm of the first order gradient <= 10^-4.',
    'Stop reason: exceed the number of iterations.',
    'Stop reason: small enough error.'
)

# ex1
# Backtracking line search algorithm
def backtrackingLineSearch(f, x, deltax, gradient, alpha=1, rho=0.8, c=0.5):
    pk = deltax
    while f(x+alpha*pk) > f(x) + c*alpha*np.dot(gradient, pk):
        alpha *= rho
    return alpha

# Gradient descent algorithm
def gradientDescent(startPoint, f=Rosembrock, gradient=firstOrderGradientOfRosembrock, iters=1000):
    x = startPoint
    count = 0
    for _ in range(iters):
        if stopCondition(x):
            return x, count, stopReasons[0]
        g1 = gradient(x)
        deltax = -g1
        t = backtrackingLineSearch(f, x, deltax, g1)
        x = x + t*deltax
        count += 1
    return x, count, stopReasons[1]

# ex2
# Newton method
def Newton(startPoint, f=Rosembrock, firstOrderGradient=firstOrderGradientOfRosembrock, secondOrderGradient=secondOrderGradientOfRosembrock, eps=10**-9, iters=1000):
    x = startPoint
    count = 0
    for _ in range(iters):
        if stopCondition(x):
            return x, count, stopReasons[0]
        g1 = firstOrderGradient(x)
        g2 = np.linalg.inv(secondOrderGradient(x))
        deltax = -np.dot(g2, g1)
        lambda2 = np.dot(g1, np.dot(g1, g2))
        if lambda2/2 <= eps:
            return x, count, stopReasons[2]
        t = backtrackingLineSearch(f, x, deltax, g1)
        x = x + t*deltax
        count += 1
    return x, count, stopReasons[1]

def calExecTime(*methods):
    re = dict()
    for method in methods:
        for startPoint in startPoints:
            startTime = time.time()
            method(startPoint=startPoint)
            endTime = time.time()
            re[method.__name__ + ' with ' + str(tuple(startPoint)) + ':'] = endTime - startTime
    return re
        
def evaluateResult(*methods):
    re = dict()
    for method in methods:
        for startPoint in startPoints:
            res = method(startPoint=startPoint)[0]
            dis = np.linalg.norm(actualResult-res)
            re[method.__name__ + ' with ' + str(tuple(startPoint)) + ':'] = dis
    return re

if __name__ == "__main__":
    numstr = 'Number of iteration: '
    l = 150
    print('Exercise 1'.center(l, '-'))
    print('Gradient descent with Backtracking Line Search')
    for startPoint in startPoints:
        re = gradientDescent(startPoint=startPoint)
        print('\tStart point: {} => {}\n\t\t{}\n\t\t{}{}'.format(tuple(startPoint), re[0], re[2], numstr, re[1]))
    print('Exercise 2'.center(l, '-'))
    print('Newton method with Backtracking Line Search')
    for startPoint in startPoints:
        re = Newton(startPoint=startPoint)
        print('\tStart point: {} => {}\n\t\t{}\n\t\t{}{}'.format(tuple(startPoint), re[0], re[2], numstr, re[1]))
    print('Exercise 3'.center(l, '-'))
    print('Evaluate')
    print('\tExecution time')
    re = calExecTime(gradientDescent, Newton)
    for k in re:
        print('\t\t', k, re[k])
    print('\tQuality of the result by Euclidean distance')
    re = evaluateResult(gradientDescent, Newton)
    for k in re:
        print('\t\t', k, re[k])