#!/usr/bin/env python

import numpy as np
import cv2

def powerTransform(inputImage, fileName, gamma):
    transformed = np.power(inputImage, gamma)
    transformed = np.array(transformed, dtype=np.uint8)
    cv2.imwrite("res4exe3gamma{0}".format(gamma) + fileName, transformed)

if __name__ == "__main__":
    fileName = input('File name?\n')
    gamma = float(input('Gamma?\n'))
    try:
        inputImage = cv2.imread(fileName)
        powerTransform(inputImage, fileName, gamma)
        print('done')
    except FileNotFoundError:
        raise FileNotFoundError("{0} not found!".format(fileName))