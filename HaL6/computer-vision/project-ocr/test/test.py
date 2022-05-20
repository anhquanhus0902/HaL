#!/usr/bin/env python

import numpy as np
import cv2

def grayscale(im):
    height, width, channels = im.shape
    grayscale_im = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            grayscale_im[i][j] = int(np.average(im[i][j]))
    return grayscale_im

def threshold(im):
    '''
    Using local maxima and minima method
    '''
    I_max = np.amax(im)
    I_min = np.amin(im)
    if I_max == I_min:
        epsilon = 0.01
    else:
        epsilon = 0
    return (I_max-I_min)/(I_max+I_min)

# Binarization
def binarization(im):
    im_threshold = 127
    im[grayscale_im <= im_threshold] = 0
    im[grayscale_im > im_threshold] = 255
    return im

if __name__ == "__main__":
    path = './girl.png'
    im = cv2.imread(path)
    bin_im = cv2.Canny(im, 100, 200)
    cv2.imwrite('res1.png', bin_im)