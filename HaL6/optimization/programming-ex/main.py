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

startPoint1 = np.array([1.2, 1.2])
startPoint2 = np.array([-1.2, 1])

# ex1
# Backtracking line search algorithm
def backtrackingLineSearch(f, x, deltax, alpha=1, rho=0.8, c=0.5):
    pk = deltax
    while f(x+alpha*pk) > f(x) + c*alpha*np.dot(-deltax, pk):
        alpha *= rho
    return alpha

# Gradient descent algorithm
def gradientDescent(startPoint, f=Rosembrock, gradient=firstOrderGradientOfRosembrock, iters=1000):
    x = startPoint
    count = 0
    for i in range(iters):
        if stopCondition(x):
            return x, count, 'Stop reason: norm of the first order gradient <= 10^-4.'
        g1 = gradient(x)
        deltax = -g1
        t = backtrackingLineSearch(f, x, deltax)
        x = x + t*deltax
        count += 1
    return x, count, 'Stop reason: numbers of iteration >= %d.' % count

# ex2
# Newton method
def Newton(startPoint, f=Rosembrock, firstOrderGradient=firstOrderGradientOfRosembrock, secondOrderGradient=secondOrderGradientOfRosembrock, eps=10**-4, iters=1000):
    x = startPoint
    count = 0
    for i in range(iters):
        if stopCondition(x):
            return x, count, 'Stop reason: norm of the first order gradient <= 10^-4.'
        g1 = firstOrderGradient(x)
        g2 = np.linalg.inv(secondOrderGradient(x))
        deltaxnt = -np.dot(g2, g1)
        lambda2 = np.dot(g1, np.dot(g1, g2))
        if lambda2/2 <= eps:
            return x, count, 'Stop reason: small enough error.'
        #t = backtrackingLineSearch(f, x, deltaxnt)
        t = 1
        x = x + t*deltaxnt
        count += 1
    return x, count, 'Stop reason: numbers of iteration >= %d.' % count

def calExecTime(*methods):
    re = dict()
    startPoints = [startPoint1, startPoint2]
    for method in methods:
        for startPoint in startPoints:
            startTime = time.time()
            method(startPoint=startPoint)
            endTime = time.time()
            re[method.__name__ + ' with ' + str(startPoint) + ':'] = endTime - startTime
    return re
        

if __name__ == "__main__":
    numstr = 'Numbers of iteration: '
    l = 150
    print('Exercise 1'.center(l, '-'))
    print('Gradient descent with Backtracking Line Search')
    res1 = gradientDescent(startPoint=startPoint1)
    res2 = gradientDescent(startPoint=startPoint2)
    print('Start point: {} => {}\n{} {}{}'.format(startPoint1, res1[0], res1[2], numstr, res1[1]))
    print('Start point: {} => {}\n{} {}{}'.format(startPoint2, res2[0], res2[2], numstr, res2[1]))
    print('Exercise 2'.center(l, '-'))
    print('Newton method with Backtracking Line Search')
    res3 = Newton(startPoint=startPoint1)
    res4 = Newton(startPoint=startPoint2)
    print('Start point: {} => {}\n{} {}{}'.format(startPoint1, res3[0], res3[2], numstr, res3[1]))
    print('Start point: {} => {}\n{} {}{}'.format(startPoint2, res4[0], res4[2], numstr, res4[1]))
    print('Exercise 3'.center(l, '-'))
    print('Evaluate')
    re = calExecTime(gradientDescent, Newton)
    for k in re:
        print(k, re[k])
