#!/usr/bin/env python

from matplotlib.pyplot import contour
import numpy as np
import cv2

def canny(im):
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mean_of_im = np.mean(grey)
    low_threshold = 0
    high_threshold = 1.33 * mean_of_im
    edgemap = cv2.Canny(im, low_threshold, high_threshold)
    return edgemap

def usm(im, radius=0, sigma=3.0, amount=1):
    blurred = cv2.GaussianBlur(im, (radius,radius), sigma)
    re = cv2.addWeighted(im, amount+1, blurred, -amount, 0)
    return re

def draw_edge_on_image_border(edgemap, bd):
    line_width = 10
    h, w = edgemap.shape
    if bd == 1:
        for i in range(line_width):
            for j in range(w):
                edgemap[i,j] = 255
    elif bd == 2:
        for i in range(h):
            for j in range(line_width):
                edgemap[i,j] = 255
    elif bd == 3:
        for i in range(h-line_width-1, h):
            for j in range(w):
                edgemap[i,j] = 255
    elif bd == 4:
        for i in range(h):
            for j in range(w-line_width-1, w):
                edgemap[i,j] = 255
    else:
        pass
    return edgemap

def find_contour_of_doc(edgemap):
    contours, hierarchy = cv2.findContours(edgemap, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    output = np.array([])
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 20000:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*perimeter, True)
            if area > max_area and len(approx) == 4:
                output = approx
                max_area = area
    return output

def size_of_doc(contour_of_doc):
    n = len(contour_of_doc)
    max_x, max_y, min_x, min_y = 0, 0, np.inf, np.inf
    for i in range(n):
        max_x = max(max_x, contour_of_doc[i][0][0])
        max_y = max(max_y, contour_of_doc[i][0][1])
        min_x = min(min_x, contour_of_doc[i][0][0])
        min_y = min(min_y, contour_of_doc[i][0][1])
    return (max_y-min_y, max_x-min_x)

def reorder(approx):
    # reshape to a 4x2 matrix
    approx = approx.reshape((4, 2))
    output = np.zeros((4, 2), dtype=np.int32)
    # get x+y of each point in approx
    add = approx.sum(1)
    # point with smallest sum
    output[0] = approx[np.argmin(add)]
    # point with biggest sum
    output[3] =approx[np.argmax(add)]
    # get x-y of each point in approx
    diff = np.diff(approx, axis=1)
    # point with smallest diff
    output[1] =approx[np.argmin(diff)]
    # point with biggest diff
    output[2] = approx[np.argmax(diff)]
    return output

def perspective_transform(im, contour_of_doc):
    h, w = size_of_doc(contour_of_doc)
    output = im
    if contour_of_doc.size != 0:
        contour_of_doc = reorder(contour_of_doc)
        pts1 = np.float32(contour_of_doc)
        pts2 = np.float32([[0, 0],[w, 0], [0, h],[w, h]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        output = cv2.warpPerspective(im, matrix, (w, h))
        output=output[10:output.shape[0] - 10, 10:output.shape[1] - 10]
        output = cv2.resize(output,(w,h))
    return output

def preprocess(im):
    #im = usm(im, 5, 1.4, 2)
    edgemap = canny(im)
    contour_of_doc = find_contour_of_doc(edgemap)
    warped = perspective_transform(im, contour_of_doc)
    return usm(warped, 5, 1.4, 2)
