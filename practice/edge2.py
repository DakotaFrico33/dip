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
    resized = imutils.resize(gray, width=args.width)
    a = put_text(resized.copy(),title='original')
    cv2.imshow("image", a)

    logger.info('Use [A],[S],[D] to increase [Z],[X],[C] to decrease values. Use [Q] to quit')
    low = 50
    high = 100
    blur = 5
    # temp bug fix for blur steps (blur must always be odd number)
    if args.offset%2==1:
        args.offset=args.offset+1

    while True:
        low,high,blur=read_key(cv2.waitKey(0) & 0xFF,k1=low,k2=high,k3=blur,offset=args.offset)
        if low == -2:
            logger.info('Pressed Q button. Exit immediately!')
            break
        elif low <= -1 or high > 255:
            logger.error('Out of bounds. Exit immediately!')
            break
        else:
            h_stack = [a]
            blurred = cv2.GaussianBlur(gray, (blur, blur), 0)
            resized = imutils.resize(blurred, width=args.width)
            b = put_text(resized.copy(),title=f'blurred ({blur},{blur})')
            h_stack.append(b)

            str = f"l={low}, h={high}"
            img_edge = cv2.Canny(blurred, low, high)
            resized = imutils.resize(img_edge, width=args.width)
            c=put_text(resized.copy(),title=f'{str}')
            h_stack.append(c)

            cv2.imshow("image", np.hstack(h_stack))
            logger.info(f'{str}, blur={blur}')

    cv2.destroyAllWindows()


if __name__ == '__main__':
    sys.exit(main())
