#!/usr/bin/env python

import numpy as np
import cv2

def canny(im):
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mean_of_im = np.mean(gray_im)
    low_threshold = 0
    high_threshold = 1.33 * mean_of_im
    edgemap = cv2.Canny(im, low_threshold, high_threshold)
    return edgemap

def usm(im, radius=0, sigma=3.0, amount=1):
    gauss3 = cv2.GaussianBlur(im, (radius,radius), sigma)
    unshapr_im = cv2.addWeighted(im, amount+1, gauss3, -amount, 0)
    return unshapr_im

def reorder(approx):
    approx = approx.reshape((4, 2))
    output = np.zeros((4, 1, 2), dtype=np.int32)
    add = approx.sum(1)
    output[0] = approx[np.argmin(add)]
    output[3] =approx[np.argmax(add)]
    diff = np.diff(approx, axis=1)
    output[1] =approx[np.argmin(diff)]
    output[2] = approx[np.argmax(diff)]
    return output

def find_contour_of_doc(im):
    edgemap = canny(im)
    contours, hierarchy = cv2.findContours(edgemap, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    output = np.array([])
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 10000:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*perimeter, True)
            if area > max_area and len(approx) == 4:
                output = approx
                max_area = area
    return output

def perspective_transform(im, contour_of_doc):
    h, w = 640, 480
    output = im
    if contour_of_doc.size != 0:
        contour_of_doc = reorder(contour_of_doc)
        pts1 = np.float32(contour_of_doc)
        pts2 = np.float32([[0, 0],[w, 0], [0, h],[w, h]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        output = cv2.warpPerspective(im, matrix, (w, h))
        output=output[20:output.shape[0] - 20, 20:output.shape[1] - 20]
        output = cv2.resize(output,(w,h))
    return output

def preprocess(im):
    # im = usm(im, 0, 1.0, 2)
    contour_of_doc = find_contour_of_doc(im)
    warped = perspective_transform(im, contour_of_doc)
    return usm(warped)