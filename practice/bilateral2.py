#!/usr/bin/env python3
# adapted from: https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/
import os
import sys

import cv2
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
    cv2.imshow("image", image)
    logger.info('Use [A],[S],[D] to increase [Z],[X],[C] to decrease size of kernel. Use [q] to quit')
    diameter = args.bilateral
    sigma_c = 21
    sigma_s = 7

    while True:
        diameter,sigma_c,sigma_s=read_key(cv2.waitKey(0) & 0xFF,k1=diameter,k2=sigma_c,k3=sigma_s,offset=args.offset)
        if diameter == -2:
            logger.info('Pressed Q button. Exit immediately!')
            break
        elif diameter <= -1:
            logger.error('Negative value. Exit immediately!')
            break
        else:
            a = put_text(image.copy(),title='original')
            h_stack = [a]

            blurred = cv2.bilateralFilter(image, diameter, sigma_c, sigma_s)
            str = f"d={diameter}, sc={sigma_c}, ss={sigma_s}"
            blurred = put_text(blurred.copy(),title=f'{str}',scale=0.7)
            h_stack.append(blurred)

            cv2.imshow("image", np.hstack(h_stack))
            logger.info(str)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    sys.exit(main())
