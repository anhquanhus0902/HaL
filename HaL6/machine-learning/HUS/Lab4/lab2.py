#!/usr/bin/env python3

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

def readData(path):
    f = open(path, 'r')
    lines = f.readlines()
    data = list()
    for line in lines:
        data.append(line.split(","))
    y = np.array([float(sample[1]) for sample in data])
    X = np.array([float(sample[0]) for sample in data])
    plt.scatter(X, y)
    plt.show()
    N = len(y)
    X_train = np.c_[np.ones(N), X]
    return (X, X_train, y)

def train(X, y):
    return np.dot(np.dot(inv(np.dot(np.transpose(X), X)), np.transpose(X)), y)

def predict(theta, xNew):
    return np.dot(theta, xNew)

def bgd(X, y, T=1000, alpha=0.1):
    thetaS = list()
    theta = np.zeros(X.shape[1])
    for i in range(T):
        g = np.dot(np.dot(np.transpose(X), X), theta) - np.dot(np.transpose(X), y)
        theta = np.array([i-alpha*g for i in theta])
        thetaS.append(theta)
    return thetaS

if __name__ == "__main__":
    X, X_train, y = readData('profits.txt')
    theta = train(X_train, y)
    plt.scatter(X, y)
    plt.plot(X, theta[1]*X+theta[0], color='black')
    plt.show()
    bgd(X_train, y)
