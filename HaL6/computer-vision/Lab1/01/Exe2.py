#!/usr/bin/env python

import numpy as np
import cv2

def img2double(img):
    info = np.iinfo(img.dtype)
    return img.astype(np.float)/info.max

if __name__ == "__main__":
    J = cv2.imread('lionHSV.jpg')
    Jh = J[:,:,2]
    B = cv2.normalize(Jh.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
    #B = img2double(Jh)
    B[B<=0.22] = 0
    B[B>=0.45] = 0
    B[B!=0] = 1
    B = cv2.convertScaleAbs(B, alpha=(255.0))
    cv2.imshow('Result', B)
    cv2.waitKey(0)
    cv2.imwrite("res4exe2.jpg", B)
