#!/usr/bin/env python3
# adapted from: https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/
import os
import sys

import cv2
import numpy as np

from arg_parse import args
from logger_setup import logger
from open_cv import put_text


###################################################################3
def main():
    image = args.image
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,image))

    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    a = put_text(blurred.copy(),title='blurred')
    h_stack = [a]
    # compute a "wide", "mid-range", and "tight" threshold for the edges
    wide = cv2.Canny(blurred, 10, 200)
    b=put_text(wide.copy(),title=f'wide')
    h_stack.append(b)

    mid = cv2.Canny(blurred, 30, 150)
    c=put_text(mid.copy(),title=f'mid')
    h_stack.append(c)

    tight = cv2.Canny(blurred, 240, 250)
    d=put_text(tight.copy(),title=f'tight')
    h_stack.append(d)

    if len(h_stack) > 1:
        cv2.imshow("image", np.hstack(h_stack))
        cv2.waitKey(0)
    else:
        logger.warning(f'No parameters for blurring were issued. Exit immediately!')

if __name__ == '__main__':
    sys.exit(main())
