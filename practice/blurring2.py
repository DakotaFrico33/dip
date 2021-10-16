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
    logger.info('Use [A] to increase [Z] to decrease size of kernel. Use [Q] to quit')
    k=args.kernel_sizes[0]

    while True:
        k,_,_=read_key(cv2.waitKey(0) & 0xFF,k1=k,offset=2)
        if k == -2:
            logger.info('Pressed Q button. Exit immediately!')
            break
        elif k <= -1:
            logger.error('Negative value. Exit immediately!')
            break
        else:
            logger.info(f'k is equal to: {k}')
            a = put_text(image.copy(),title='original')
            h_stack = [a]

            if args.blurred:
                kX=k
                kY=k
                blurred = cv2.blur(image, (kX, kY))
                b = put_text(blurred.copy(),title=f'average ({kX},{kY})')
                h_stack.append(b)

            if args.gaussian:
                kX=k
                kY=k
                gaussian = cv2.GaussianBlur(image, (kX, kY), 0)
                c = put_text(gaussian.copy(),title=f'gaussian ({kX},{kY})')
                h_stack.append(c)

            if args.median:
                gaussian = cv2.medianBlur(image, k)
                d = put_text(gaussian.copy(),title=f'median ({k})')
                h_stack.append(d)
            cv2.imshow("image", np.hstack(h_stack))

    cv2.destroyAllWindows()


if __name__ == '__main__':
    sys.exit(main())
