#!/usr/bin/env python3
import sys
from math import sqrt

import numpy as np
from arg_parse import args
from logger_setup import logger


def _split_into_blocks(img, block_size=2):
    blocks=np.ones((img.shape[0]*img.shape[1]//(block_size**2),
                    block_size,
                    block_size),dtype=np.uint8)*(-1)
    logger.debug(blocks.shape)

    if img.shape[0] % block_size != 0:
        logger.error(f"Invalid block size: sizes of image (W={img.shape[0]}) and DCT block (size={block_size}) do not match")
        sys.exit()

    if img.shape[1] % block_size != 0:
        logger.error(f"Invalid block size: sizes of image (H={img.shape[1]}) and DCT block (size={block_size}) do not match")
        sys.exit()

    for j,row in enumerate(range(0,img.shape[0],block_size)):
        for k,col in enumerate(range(0,img.shape[1],block_size)):
            block = img[row:row+block_size, col:col+block_size]
            idx = j*(img.shape[1]//block_size)+k
            blocks[idx] = block
    return blocks


def _reshape(blocks, block_size):
    num_blocks = int(sqrt(len(blocks)))

    logger.debug(blocks.shape)

    blocks = blocks.reshape(num_blocks,num_blocks,block_size,block_size)
    logger.debug(blocks.shape)

    blocks = np.hstack(blocks)
    logger.debug(blocks.shape)

    blocks = np.concatenate(blocks,axis=1)
    logger.debug(blocks.shape)
    return blocks


def _func_sum(block,j,k,C=None,inverse=False):
    N = block.shape[0]
    val = 0
    for x,row in enumerate(block):
        for y,num in enumerate(row):
            if not inverse:
                C_j = C[0] if j==0 else C[1]
                C_k = C[0] if k==0 else C[1]
                val += num * np.cos(((2*x+1)*j*np.pi)/(2*N)) * np.cos(((2*y+1)*k*np.pi)/(2*N))
                if args.test:
                    logger.debug(f"C_j={C_j}, C_k={C_k} | num={num} | x={x},j={j},y={y},k={k}")
            else:
                C_j = C[0] if x==0 else C[1]
                C_k = C[0] if y==0 else C[1]
                val += C_j * C_k * num * np.cos(((2*j+1)*x*np.pi)/(2*N)) * np.cos(((2*k+1)*y*np.pi)/(2*N))
                if args.test:
                    logger.debug(f"C_j={C_j}, C_k={C_k} | num={num} | x={j},j={x},y={k},k={y}")

    if not inverse:
        val *= C_j * C_k
    return val


def dct_2d(img, block_size=2, inverse = False):
    blocks = _split_into_blocks(img, block_size=block_size)
    blocks_mod = np.empty_like(blocks)
    coeff = [np.sqrt(1/block_size), np.sqrt(2/block_size)]
    for i,block in enumerate(blocks):
        block_mod = np.empty_like(block, dtype=np.int16)
        for j,row in enumerate(block):
            for k,_ in enumerate(row):
                sum_of_nums = _func_sum(block,j,k,C=coeff,inverse=inverse)
                val = 2/block_size*sum_of_nums
                block_mod[j,k] = val
            pass
        blocks_mod[i] = block_mod
        if not args.test:
            if i%(len(blocks)//4) == 0:
                logger.debug(i)
    logger.debug(i)

    blocks_mod = _reshape(blocks_mod, block_size=block_size)
    return blocks_mod


def dct_1d():
    pass


def dct_fast():
    pass
