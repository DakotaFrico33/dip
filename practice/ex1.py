#!/usr/bin/env python3
import sys

import imutils
import cv2

from arg_parse import args
from logger_setup import logger


def main():
    # load the input image and show its dimensions, keeping in mind that
    # images are represented as a multi-dimensional NumPy array with
    # shape no. rows (height) x no. columns (width) x no. channels (depth)
    image = cv2.imread("lena.png")
    (h, w, d) = image.shape
    print("width={}, height={}, depth={}".format(w, h, d))

    # manually computing the aspect ratio can be a pain so let's use the
    # imutils library instead
    resized = imutils.resize(image, width=300)
    cv2.imshow("Imutils Resize", resized)
    cv2.waitKey(0)


    # apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
    # useful when reducing high frequency noise
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    cv2.imshow("Blurred", blurred)
    cv2.waitKey(0)


    # draw a 2px thick red rectangle surrounding the face
    output = image.copy()
    cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
    cv2.imshow("Rectangle", output)
    cv2.waitKey(0)


    # draw green text on the image
    output = image.copy()
    cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25),
    	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Text", output)
    cv2.waitKey(0)

if __name__ == '__main__':
    sys.exit(main())
