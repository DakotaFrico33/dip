#!/usr/bin/env python3
import numpy as np

from logger_setup import logger

# Implementation of 2D­ DCT and its inverse transform
# Additional bonus for these options:
# + implement 1D
# + Fast DCT Algorithm

def _split_into_blocks(img, block_size=2):
    blocks=np.zeros((img.shape[0]//block_size,
                    img.shape[1]//block_size,
                    block_size,
                    block_size),dtype=np.uint8)
    logger.debug(blocks.shape)

    for j,row in enumerate(range(0,img.shape[0],block_size)):
        for k,col in enumerate(range(0,img.shape[1],block_size)):
            block = img[row:row+block_size, col:col+block_size]
            blocks[j,k] = block
    return blocks

def dct_2d(img, args):
    blocks = _split_into_blocks(img, block_size=8)
    return img

def idct_2d():
    pass

def dct_1d():
    pass

def dct_fast():
    pass
