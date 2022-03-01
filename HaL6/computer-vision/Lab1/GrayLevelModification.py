#!/usr/bin/env python

import numpy as np
import cv2

def grayLevelModification(inputImage, fileName):
    transformed = 16 * np.sqrt(inputImage)
    transformed = np.array(transformed, dtype=np.uint8)
    # outputImage = Image.fromarray(transformed)
    # outputImage.show()
    cv2.imwrite("res4exe1" + fileName, transformed)

if __name__ == "__main__":
    fileName = input('File name?\n')
    try:
        inputImage = cv2.imread(fileName)
        # Image.open(fileName).show()
        grayLevelModification(inputImage, fileName)
        print('done')
    except FileNotFoundError:
        raise FileNotFoundError("{0} not found!".format(fileName))