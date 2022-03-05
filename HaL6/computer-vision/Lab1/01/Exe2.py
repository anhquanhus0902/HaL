#!/usr/bin/env python

import numpy as np
import cv2

if __name__ == "__main__":
    J = cv2.imread('lionHSV.jpg')
    B = J.copy()
    B[:,:,0] = 0
    B[:,:,1] = 0
    w, l = B[:,:,2].shape
    #cv2.imshow('xxx', B)
    #cv2.waitKey(0)
    #for i in range(w):
    #    for j in range(l):
    #        if B[i,j,2]/255 > 0.22 and B[i,j,2]/255 < 0.45:
    #            B[i,j,2] = 255
    #        else:
    #            B[i,j,2] = 0
    cv2.imshow('xxx', B)
    cv2.waitKey(0)
    # cv2.imwrite("res4exe2.jpg", B)
