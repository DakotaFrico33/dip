#!/usr/bin/env python3
import sys
from math import sqrt

import numpy as np
from arg_parse import args
from logger_setup import logger


def _split_into_blocks(img: np.array, n=2):
    '''
    Split image into blocks of size n-by-n
    '''
    blocks=np.ones((img.shape[0]*img.shape[1]//(n**2),
                    n,
                    n),dtype=np.uint8)*(-1)

    if img.shape[0] % n != 0:
        logger.error(f"Invalid block size: sizes of image (W={img.shape[0]}) and DCT block (size={n}) do not match")
        sys.exit()

    if img.shape[1] % n != 0:
        logger.error(f"Invalid block size: sizes of image (H={img.shape[1]}) and DCT block (size={n}) do not match")
        sys.exit()

    for j,row in enumerate(range(0,img.shape[0],n)):
        for k,col in enumerate(range(0,img.shape[1],n)):
            block = img[row:row+n, col:col+n]
            idx = j*(img.shape[1]//n)+k
            blocks[idx] = block
    return blocks


def _reshape(blocks, n):
    '''
    From 3D input array, reconstruct 2D image

    Input (3D)          : several blocks (of size n-by-n) in one single column
    Step 1 (3D -> 4D)   : arrange blocks into rows of equal length
    Step 2 (4D -> 3D)   : stack blocks horizontally
    Step 3 (3D -> 2D)   : concatenate blocks column-wise
    Output (2D)         : 2D image (1 blocks of size N-by-N)
    '''
    logger.debug(blocks.shape)

    blocks = blocks.reshape(int(sqrt(len(blocks))),int(sqrt(len(blocks))),n,n)
    logger.debug(blocks.shape)

    blocks = np.hstack(blocks)
    logger.debug(blocks.shape)

    blocks = np.concatenate(blocks,axis=1)
    logger.debug(blocks.shape)

    return blocks


def dct_2d(img, block_size=2, inverse = False):
    '''
    Execute Basic 2D Discrete Cosine Transform.
    If triggered (inverse = True), do the Inverse DCT instead.

    Reference: Dr. Guo's lecture (chapter 7, slides [92,93])
    '''
    blocks = _split_into_blocks(img, n=block_size)
    blocks_mod = np.empty_like(blocks)
    C = [np.sqrt(1/block_size), np.sqrt(2/block_size)]

    for i,block in enumerate(blocks):
        block_mod = np.empty_like(block, dtype=np.int16)
        # DCT
        if not inverse:
            for j,row in enumerate(block):
                for k,_ in enumerate(row):
                    val = 0
                    C_j = C[0] if j==0 else C[1]
                    C_k = C[0] if k==0 else C[1]
                    for x,row in enumerate(block):
                        for y,num in enumerate(row):
                            cos1 = np.cos(((2*x+1)*j*np.pi)/(2*block_size))
                            cos2 = np.cos(((2*y+1)*k*np.pi)/(2*block_size))
                            val += num * cos1 * cos2
                    block_mod[j,k] = 2 / block_size * C_j * C_k * val
        # IDCT
        else:
            for x,row in enumerate(block):
                for y,_ in enumerate(row):
                    val = 0
                    for j,row in enumerate(block):
                        for k,num in enumerate(row):
                            C_j = C[0] if j==0 else C[1]
                            C_k = C[0] if k==0 else C[1]
                            cos1 = np.cos(((2*x+1)*j*np.pi)/(2*block_size))
                            cos2 = np.cos(((2*y+1)*k*np.pi)/(2*block_size))
                            val += C_j * C_k * num * cos1 * cos2
                    block_mod[x,y] = 2 / block_size * val
        blocks_mod[i] = block_mod

    blocks_mod = _reshape(blocks_mod, n=block_size)
    return blocks_mod


def dct_1d():
    pass


def dct_fast():
    pass
