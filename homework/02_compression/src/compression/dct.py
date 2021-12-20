#!/usr/bin/env python3
from math import sqrt
import numpy as np

from logger_setup import logger

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

def _func_sum(block,j,k):
    val = 0
    N = block.shape[0]
    for x,row in enumerate(block):
        for y,num in enumerate(row):
            val += num * np.cos(((2*x+1)*j*np.pi)/(2*N)) * np.cos(((2*y+1)*k*np.pi)/(2*N))
    return val


def dct_2d(img, block_size=2):
    blocks = _split_into_blocks(img, block_size=block_size)
    blocks_original = blocks
    coeff = [np.sqrt(1/block_size), np.sqrt(2/block_size)]
    for i,block in enumerate(blocks_original):
        block_modified = np.empty_like(block, dtype=np.int16)
        for j,row in enumerate(block):
            for k,_ in enumerate(row):
                C_j = coeff[0] if j==0 else coeff[1]
                C_k = coeff[0] if k==0 else coeff[1]
                sum_of_nums = _func_sum(block,j,k)
                val = 2/block_size*C_j*C_k*sum_of_nums
                # for puproses of showing the DCT block-image restrict values from 0 to 255. #TODO: differentiate real np out (to feed to IDCT) from np used for saving image
                val = 255 if val > 255 else int(val)
                val = 0 if val < 0 else int(val)
                block_modified[j,k] = val
            pass
        blocks[i] = block_modified
        if i%50 == 0:
            logger.debug(i)
    logger.debug(i)

    num_blocks = int(sqrt(len(blocks)))
    logger.debug(blocks.shape)
    a0 = blocks[0]
    a1 = blocks[num_blocks]
    a2 = blocks[-1]

    blocks = blocks.reshape(num_blocks,num_blocks,block_size,block_size)
    logger.debug(blocks.shape)
    b0 = blocks[0,0]
    b1 = blocks[1,0]
    b2 = blocks[-1,-1]

    msgs = [ "True" if (a0==b0).all() else "False",
            "True" if (a1==b1).all() else "False",
            "True" if (a2==b2).all() else "False"]

    for msg in msgs:
        logger.debug(msg)

    blocks = np.hstack(blocks)
    logger.debug(blocks.shape)
    blocks = np.concatenate(blocks,axis=1)
    logger.debug(blocks.shape)
    return blocks

def idct_2d():
    pass

def dct_1d():
    pass

def dct_fast():
    pass
