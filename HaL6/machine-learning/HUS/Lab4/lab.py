#!/usr/bin/env python3

import numpy as np
from numpy.linalg import inv

def readData(path):
    f = open(path, 'r')
    lines = f.readlines()
    data = list()
    for line in lines:
        data.append(line.split(','))
    y = np.array([float(sample[1]) for sample in data])
    X = np.array([float(sample[0]) for sample in data])
    N = len(y)
    X = np.c_[np.ones(N), X]
    return (X, y)

def train(X, y):
    return np.dot(np.dot(inv(np.dot(np.transpose(X), X)), np.transpose(X)), y)

def gradientDescent(theta):
    pass

def predict(theta, xNew):
    return np.dot(theta, xNew)

if __name__ == "__main__":
    X, y = readData('./profits.txt')
    theta = train(X, y)
    print(predict(theta, np.array([1, 6.1101])))
