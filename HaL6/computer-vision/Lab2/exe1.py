#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    I = cv2.imread('images.jpg')
    J = cv2.imread('binary.png')
    sizeJ1, sizeJ2, sizeJ3 = J.shape
    I = cv2.resize(I, (sizeJ2, sizeJ1))
    sizeI1, sizeI2, sizeI3 = I.shape

    dbI = I/255
    dbI = np.array(dbI, dtype=np.uint8)

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    imgplot1 = plt.imshow(dbI)
    ax.set_title(str(sizeI1)+"x"+str(sizeI2)+"x"+str(sizeI3))

    ax = fig.add_subplot(1, 2, 2)
    imgplot2 = plt.imshow(J)
    ax.set_title(str(sizeJ1)+"x"+str(sizeJ2))
    plt.savefig('res4exe1.jpg')
