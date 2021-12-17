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

def _func_sum(block,j,k):
    val = 0
    N = block.shape[0]
    for x,row in enumerate(block):
        for y,num in enumerate(row):
            val += num * np.cos(((2*x+1)*j*np.pi)/(2*N)) * np.cos(((2*y+1)*k*np.pi)/(2*N))
    return val


def dct_2d(img, args):
    block_size = 8
    blocks = _split_into_blocks(img, block_size=block_size)
    blocks_original = blocks
    coeff = [np.sqrt(1/block_size), np.sqrt(2/block_size)]
    for i,block in enumerate(blocks):
        block_original = block
        for j,row in enumerate(block):
            for k,_ in enumerate(row):
                if j==0:
                    C_j = coeff[0]
                else:
                    C_j = coeff[1]

                if k==0:
                    C_k = coeff[0]
                else:
                    C_k = coeff[1]

                sum_of_nums = _func_sum(block_original,j,k)
                block[j,k] = 2/block_size*C_j*C_k*sum_of_nums
                pass
            pass
        blocks[i] = block
        print(i)
        pass
    print(blocks)
    print(block.shape)
    return img

def idct_2d():
    pass

def dct_1d():
    pass

def dct_fast():
    pass
