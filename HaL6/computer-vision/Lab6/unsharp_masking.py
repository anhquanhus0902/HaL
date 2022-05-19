#!/usr/bin/env python

import numpy as np
import cv2
from scipy.ndimage import convolve

def usm(im, sigma=0):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), sigma)
    mask = gray-blur
    return gray+1.2*mask

if __name__ == "__main__":
    path = 'girl.png'
    im = cv2.imread(path)
    res = usm(im)
    cv2.imwrite('res2'+path, res)
    cv2.imshow('test', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()