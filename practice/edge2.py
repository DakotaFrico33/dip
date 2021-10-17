#!/usr/bin/env python3
# adapted from: https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/
import os
import sys

import cv2
import imutils
import numpy as np

from arg_parse import args
from logger_setup import logger
from open_cv import put_text, read_key


###################################################################3
def main():
    image = args.image
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,image))

    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    resized = imutils.resize(blurred, width=300)
    cv2.imshow("image", resized)
    logger.info('Use [A],[S] to increase [Z],[X] to decrease size of kernel. Use [Q] to quit')
    low = 50
    high = 100

    while True:
        low,high,_=read_key(cv2.waitKey(0) & 0xFF,k1=low,k2=high,offset=args.offset)
        if low == -2:
            logger.info('Pressed Q button. Exit immediately!')
            break
        elif low <= -1 or high > 255:
            logger.error('Out of bounds. Exit immediately!')
            break
        else:
            resized = imutils.resize(blurred, width=args.width)
            a = put_text(resized.copy(),title='original')
            h_stack = [a]

            str = f"l={low}, h={high}"
            img_edge = cv2.Canny(blurred, low, high)
            resized = imutils.resize(img_edge, width=args.width)
            b=put_text(resized.copy(),title=f'{str}')
            h_stack.append(b)

            cv2.imshow("image", np.hstack(h_stack))
            logger.info(str)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    sys.exit(main())
