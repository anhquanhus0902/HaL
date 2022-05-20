#!/usr/bin/env python

import traceback
import numpy as np
import cv2
from scipy.ndimage import convolve

def grayscale(im):
    height, width, channels = im.shape
    grayscale_im = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            grayscale_im[i][j] = int(np.average(im[i][j]))
    return grayscale_im
    
def sobel(im):
    Kx = np.array([[-1,0,1], [-2,0,2], [-1,0,1]], np.float32)
    Ky = np.transpose(Kx)
    Gx = convolve(im, Kx)
    Gy = convolve(im, Ky)
    gradient = np.hypot(Gx, Gy)
    gradient = gradient / gradient.max() * 255
    theta = np.arctan2(Gy, Gx)
    angle = theta * 180.0 / np.pi
    angle[angle < 0] += 180.0
    return gradient, angle
    
def prewitt(im):
    Kx = np.array([[-1,0,1], [-1,0,1], [-1,0,1]], np.float32)
    Ky = transpose(Kx)
    Gx = convolve(im, Kx)
    Gy = convolve(im, Ky)
    gradient = np.hypot(Gx, Gy)
    gradient = gradient / gradient.max() * 255
    theta = np.arctan2(Gy, Gx)
    angle = theta * 180.0 / np.pi
    angle[angle < 0] += 180.0
    return gradient, angle

def gaussian_kernel(size, sigma):
    if sigma == None:
        sigma = size/3
    size //= 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    a = 1/(2.0 * np.pi * sigma**2)
    kernel = a * np.exp(-((x**2 + y**2)/(2.0 * sigma**2)))
    return kernel

def gaussian_filter(im, k_size=5, sigma=None):
    # M = np.array([
    #     [2, 4, 5, 4, 2],
    #     [4, 9, 12, 9, 4],
    #     [5, 12, 15, 12, 5],
    #     [4, 9, 12, 9, 4],
    #     [2, 4, 5, 4, 2]
    # ], np.float64)
    # M /= np.sum(M)
    kernel = gaussian_kernel(k_size, sigma)
    return convolve(im, kernel)
    
def non_maximum_suppression(gradient_im, angle):
    h, w = gradient_im.shape
    res_im = np.zeros((h,w))
    for i in range(1, h-1):
        for j in range(1, w-1):
            if (0 <= angle[i][j] and angle[i][j] < 22.5) or (157.5 <= angle[i][j] and angle[i][j] <= 180):
                fr, bh = gradient_im[i][j-1], gradient_im[i][j+1]
            elif 22.5 <= angle[i][j] and angle[i][j] < 67.5:
                fr, bh = gradient_im[i-1][j+1], gradient_im[i+1][j-1]
            elif 67.5 <= angle[i][j] and angle[i][j] < 112.5:
                fr, bh = gradient_im[i-1][j], gradient_im[i+1][j]
            elif 112.5 <= angle[i][j] and angle[i][j] < 157.5:
                fr, bh = gradient_im[i-1][j-1], gradient_im[i+1][j+1]
            if gradient_im[i][j] >= fr and gradient_im[i][j] >= bh:
                res_im[i][j] = gradient_im[i][j]
            else:
                res_im[i][j] = 0
    return res_im
    
def neighbor_check(im, i, j, high_threshold):
    r = [i-1,i,i+1]
    c = [j-1,j,j+1]
    neighbors = list()
    for k in r:
        for l in c:
            neighbors.append(im[k][l])
    return any(neighbor > high_threshold for neighbor in neighbors)
    
def hysteresis_thresholding(im, low_threshold, high_threshold):
    h, w = im.shape
    for i in range(1, h-1):
        for j in range(1, w-1):
            if im[i][j] > high_threshold:
                im[i][j] = 255
            elif im[i][j] >= low_threshold and im[i][j] <= high_threshold:
                if neighbor_check(im, i, j, high_threshold) == True:
                    im[i][j] = 255
                else:
                    im[i][j] = 0
            else:
                im[i][j] = 0
    return im

def canny(im, low_threshold, high_threshold):
    gray_scaled_im = grayscale(im)
    blurred_im = gaussian_filter(gray_scaled_im, 5, 1.4)
    gradient, angle = sobel(blurred_im)
    thinned_edge_im = non_maximum_suppression(gradient, angle)
    return hysteresis_thresholding(thinned_edge_im, low_threshold, high_threshold)

if __name__ == "__main__":
    try:
        im = cv2.imread('./girl.png')
        im = grayscale(im)
        test_im, the = sobel(im)
        cv2.imwrite('testxxx.png', test_im)
        cv2.imshow('test', test_im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception:
        traceback.print_exc()