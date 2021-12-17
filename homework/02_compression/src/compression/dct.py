#!/usr/bin/env python3
import numpy as np

from logger_setup import logger

# Implementation of 2D­ DCT and its inverse transform
# Additional bonus for these options:
# + implement 1D
# + Fast DCT Algorithm

def _split_into_blocks(img, block_size=2):
    blocks=np.ones((img.shape[0]*img.shape[1]//(block_size**2),
                    block_size,
                    block_size),dtype=np.uint8)*(-1)
    logger.debug(blocks.shape)

    if img.shape[0] % block_size != 0:
        logger.error("Invalid block size: sizes of image and DCT block do not match")

    if img.shape[1] % block_size != 0:
        logger.error("Invalid block size: sizes of image and DCT block do not match")

    for j,row in enumerate(range(0,img.shape[0],block_size)):
        for k,col in enumerate(range(0,img.shape[1],block_size)):
            block = img[row:row+block_size, col:col+block_size]
            idx = j*(img.shape[1]//block_size)+k
            blocks[idx] = block
    return blocks

def dct_2d(img, args):
    blocks = _split_into_blocks(img, block_size=8)
    for block in blocks:
        for row in block:
            for num in row:
                pass
            pass
        pass
    print(block)
    print(block.shape)
    return img

def idct_2d():
    pass

def dct_1d():
    pass

def dct_fast():
    pass
