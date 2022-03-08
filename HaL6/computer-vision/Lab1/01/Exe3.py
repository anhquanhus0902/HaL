#!/usr/bin/env python

import numpy as np
import cv2

def chromaKeying(imgFile, dataFile):
    img = cv2.imread(imgFile)
    with open(dataFile) as file:
        data = [line.split() for line in file]

    m, n, o = img.shape
    K1 = np.zeros((m, n))
    K2 = np.zeros((m, n))
    K3 = np.zeros((m, n))
    K = np.zeros((m, n, 3))

    for j in range(1, n+1):
        count = 0
        for i in range((j-1)*m+1, j*m+1):
            if data[i-1][3] == 1:
                K1[count][j-1] = 0
                K2[count][j-1] = 0
                K3[count][j-1] = 0
            else:
                K1[count][j-1] = data[i-1][0]
                K2[count][j-1] = data[i-1][1]
                K3[count][j-1] = data[i-1][2]
            count += 1
    K[:,:,0] = K1
    K[:,:,1] = K2
    K[:,:,2] = K3
    cv2.imshow('Result', K)
    cv2.waitKey(0)
    cv2.imwrite('res4exe3.jpg', K)

if __name__ == "__main__":
    chromaKeying("lion.jpg", "data.txt")
