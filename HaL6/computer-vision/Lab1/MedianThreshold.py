#!/usr/bin/env python

import numpy as np
import cv2

def medianThreshold(inputImage, fileName):
    hist = cv2.calcHist([inputImage], [0], None, [256], [0, 256])
    hist = np.array(hist, dtype=np.uint8)
    threshold = np.median(hist)
    transformed = inputImage.copy()
    transformed[transformed < threshold] = 0
    transformed[transformed >= threshold] = 255
    cv2.imwrite("res4exe2" + fileName, transformed)


if __name__ == "__main__":
    fileName = input('File name?\n')
    try:
        inputImage = cv2.imread(fileName)
        medianThreshold(inputImage, fileName)
        print('done')
    except FileNotFoundError:
        raise FileNotFoundError("{0} not found!".format(fileName))