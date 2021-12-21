#!/usr/bin/env python3
import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np

from arg_parse import args
from logger_setup import logger

from compression.dct import dct_2d, idct_2d

# os.environ['DISPLAY'] = ':0'

def main():
    # Load image
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,args.image))
    original = cv2.imread(args.image)
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # Apply DCT algorithm for compression
    img_dct = dct_2d(gray, args.block_size)
    img_idct = idct_2d(img_dct, args.block_size)

    #TODO: IDCT_2D

    logger.debug(gray.shape)
    logger.debug(img_dct.shape)
    logger.debug(img_idct.shape)

    if args.save:
        # Save input image and the respective DCT transformation
        save_dir = args.image.split('.tif')[0]

        cv2.imwrite(f"{save_dir}/0.png",gray)
        cv2.imwrite(f"{save_dir}/dct_2d/{args.block_size}.png",img_dct)
        cv2.imwrite(f"{save_dir}/idct_2d/{args.block_size}.png",img_idct)

    if args.show: #!THIS SECTION NOT WORKING PROPERLY AS 2ND IMAGE SHOWS AS GRAY WINDOW (USE args.save INSTEAD FOR NOW)
        cv2.imshow("gray",gray)
        cv2.waitKey(0)

        cv2.imshow("out",img_dct)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    return

if __name__ == '__main__':
    sys.exit(main())
