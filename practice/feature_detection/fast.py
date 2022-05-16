#!/usr/bin/env python3
import sys

import imutils
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# from arg_parse import args
# from logger_setup import logger


def main():
    img = cv.imread('03.jpg',0)
    img = imutils.resize(img, width=64)

    # Blur
    img = cv.GaussianBlur(img, (9,9), 0)

    # Initiate FAST object with default values
    fast = cv.FastFeatureDetector_create()

    # find and draw the keypoints
    kp = fast.detect(img,None)
    img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

    # Print all default params
    print( "Threshold: {}".format(fast.getThreshold()) )
    print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
    print( "neighborhood: {}".format(fast.getType()) )
    print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
    cv.imwrite('fast_true.png', img2)

    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)
    print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
    img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
    cv.imwrite('fast_false.png', img3)
    return

if __name__ == '__main__':
    sys.exit(main())
