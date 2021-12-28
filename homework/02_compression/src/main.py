#!/usr/bin/env python3
import logging
import os
import sys
import time

import cv2
import numpy as np

from arg_parse import args
from compression.dct import dct_2d
from logger_setup import logger

# os.environ['DISPLAY'] = ':0'

def main():
    # Load image
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,args.image))
    original = cv2.imread(args.image)
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # Apply DCT algorithm for compression
    img_dct = dct_2d(gray, args.block_size)
    logger.debug(f"Image DCT shape: {img_dct.shape}")

    img_idct = dct_2d(img_dct, args.block_size, inverse=True)
    logger.debug(f"Image IDCT shape: {img_idct.shape}")

    # Save input image and the respective DCT transformation
    if args.save:
        subdir = time.strftime('%Y%m%d')
        formats = ['tif','png']
        for format in formats:
            if format in args.image:
                break
        save_dir = args.image.split(f'.{format}')[0] + '/' + subdir

        try:
            assert os.path.exists(save_dir)
        except AssertionError:
            os.makedirs(save_dir)

        cv2.imwrite(f"{save_dir}/0.png",gray)
        cv2.imwrite(f"{save_dir}/dct_2d_{args.block_size}.png",img_dct)
        cv2.imwrite(f"{save_dir}/idct_2d_{args.block_size}.png",img_idct)
        logger.info(f"Successfully saved in: {save_dir}")

    if args.show:
        cv2.imshow("gray",gray)
        cv2.waitKey(0)

        cv2.imshow("idct",img_idct)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    return

if __name__ == '__main__':
    sys.exit(main())
