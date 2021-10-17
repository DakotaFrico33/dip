#!/usr/bin/env python3
# from: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
from itertools import zip_longest
import os
import sys

import cv2
import imutils
import numpy as np

from arg_parse import args
from logger_setup import logger
from open_cv import put_text


def kernel_sizes():
    a = args.kernel_sizes
    ks = []
    for n in a:
        if (n % 2) == 0:
            logger.warning(f"Please use only positive odd integers to define kernel sizes. Value {n} skipped")
            continue
        ks.append((n,n))
    print(ks)
    return ks

###################################################################3
def main():
    image = args.image
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,image))

    image = cv2.imread(image)
    resized = imutils.resize(image, width=args.width)
    a = put_text(resized.copy(),title='original',scale=0.5)
    h_stack = [a]
    cv2.imshow("bilateral blurring",np.hstack(h_stack))
    # cv2.waitKey(0)

    n = args.bilateral
    params = [(n, 21, 7), (n, 41, 21), (n, 61, 39)]
    for (diameter, sigma_c, sigma_s) in params:
        blurred = cv2.bilateralFilter(image, diameter, sigma_c, sigma_s)
        str = f"Blurred d={diameter}, sc={sigma_c}, ss={sigma_s}"
        resized = imutils.resize(blurred, width=args.width)
        b = put_text(resized.copy(),title=f'{str}',scale=0.5)
        h_stack.append(b)
        cv2.imshow('bilateral blurring', np.hstack(h_stack))
    cv2.waitKey(0)

if __name__ == '__main__':
    sys.exit(main())
