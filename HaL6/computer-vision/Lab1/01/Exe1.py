#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

if __name__ == "__main__":
    img1 = mpimg.imread('lion.jpg')
    img2 = mpimg.imread('lionHSV.jpg')

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    imgplot1 = plt.imshow(img1)
    ax.set_title('lion.jpg')

    ax = fig.add_subplot(1, 2, 2)
    imgplot2 = plt.imshow(img2)
    ax.set_title('lionHSV.jpg')
    plt.savefig('res4exe1.jpg')