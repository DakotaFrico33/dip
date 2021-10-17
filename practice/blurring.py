#!/usr/bin/env python3
# adapted from: https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/
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
    cv2.imshow("image",np.hstack([image]))
    # cv2.waitKey(0)

    for (kX, kY) in kernel_sizes():
        resized = imutils.resize(image, width=args.width)
        a = put_text(resized.copy(),title='original')
        h_stack = [a]

        if args.blurred:
            blurred = cv2.blur(image, (kX, kY))
            resized = imutils.resize(blurred, width=args.width)
            b = put_text(resized.copy(),title=f'average ({kX},{kY})')
            h_stack.append(b)

        if args.gaussian:
            gaussian = cv2.GaussianBlur(image, (kX, kY), 0)
            resized = imutils.resize(gaussian, width=args.width)
            c = put_text(resized.copy(),title=f'gaussian ({kX},{kY})')
            h_stack.append(c)

        if args.median:
            k = kX
            median = cv2.medianBlur(image, k)
            resized = imutils.resize(median, width=args.width)
            d = put_text(resized.copy(),title=f'median ({k})')
            h_stack.append(d)


        if len(h_stack) > 1:
            cv2.imshow("image", np.hstack(h_stack))
            cv2.waitKey(0)
        else:
            logger.warning(f'No parameters for blurring were issued. Exit immediately!')
            break

if __name__ == '__main__':
    sys.exit(main())
