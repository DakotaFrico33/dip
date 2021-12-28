#!/usr/bin/env python3
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
    if args.test:
        if args.block_size == 2:
            gray = np.array([[8,5],[3,4]])
        elif args.block_size == 4:
            gray = np.array([[8,5,8,5],[3,4,3,4],[8,5,8,5],[3,4,3,4]])
        else:
            sys.exit()

    # Apply DCT algorithm for compression
    logger.debug(f"Gray shape: {gray.shape}")

    img_dct = dct_2d(gray, args.block_size)
    logger.debug(f"Image DCT shape: {img_dct.shape}")

    img_idct = dct_2d(img_dct, args.block_size, inverse=True)
    logger.debug(f"Image IDCT shape: {img_idct.shape}")

    # Quickly verify results from algorithm
    a = 0
    b = a+args.block_size
    logger.debug(f"Show blocks of size {b-a} X {b-a} at index ({a},{a})")
    logger.debug(f"Show Original:\n {gray[a:b,a:b]}")
    logger.debug(f"Show DCT:\n {img_dct[a:b,a:b]}")
    logger.debug(f"Show IDCT:\n {img_idct[a:b,a:b]}")

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

    return

if __name__ == '__main__':
    sys.exit(main())
