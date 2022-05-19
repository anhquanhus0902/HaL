#!/usr/bin/env python

import numpy as np
import cv2
from scipy.ndimage import convolve

# todo: unsharp masking

def laplace(im):
    grayIm = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    K = np.array([[0,1,0], [1,-4,1], [0,1,0]], np.float32)
    return convolve(grayIm, K)

if __name__ == "__main__":
    path = 'girl.png'
    im = cv2.imread(path)
    res = laplace(im)
    cv2.imwrite('res-'+path, res)
    cv2.imshow('test', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    