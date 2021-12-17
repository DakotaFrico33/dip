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
    image_out = dct_2d(gray, args)
    logger.debug(original.shape)
    logger.debug(gray.shape)
    logger.debug(image_out.shape)

    if args.save:
        # Save images and their respective histograms
        save_dir = args.image.split('.tif')[0]

        cv2.imwrite(f"{save_dir}/0.png",gray)
        cv2.imwrite(f"{save_dir}/1.png",image_out)

    if args.show:
        cv2.imshow("gray",gray)
        cv2.waitKey(0)

        cv2.imshow("out",image_out)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    return

if __name__ == '__main__':
    sys.exit(main())
