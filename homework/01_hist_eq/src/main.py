#!/usr/bin/env python3
import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np

from arg_parse import args
from logger_setup import logger

os.environ['DISPLAY'] = ':0'

def plt_plot(x, y, title='title', xlabel='x', ylabel='y'):
    fig = plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x,y)
    return fig


def plt_bar(x, height, title='title', xlabel='x', ylabel='y'):
    fig = plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.bar(x,height)
    return fig


def main():
    # Step 0.1
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,args.image))
    original = cv2.imread(args.image)
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # Step 0.2
    gray_flat = gray.flatten()
    logger.debug(original.shape)
    logger.debug(gray.shape)
    logger.debug(gray_flat.shape)

    logger.debug(f'MIN: {min(gray_flat)}, MAX: {max(gray_flat)}, bits: {args.bits}, N: {2**args.bits}')
    if 2**args.bits < max(gray_flat):
        logger.error('increase number of bits')
        return

    # Step 0.3
    r_i = np.arange(0,2**args.bits)
    r_i_count = np.zeros(r_i.shape, dtype=np.uint64)
    r_sum = np.zeros(r_i_count.shape, dtype=np.uint64)
    s_i = np.zeros(r_i_count.shape, dtype=np.uint8)
    s_i_count = np.zeros(r_i.shape, dtype=np.uint64)

    # Step 1. Count occurences of same pixel value
    for pixel in gray_flat:
        r_i_count[pixel] += 1
    try:
        logger.debug(f'MIN: {min(gray_flat)} --> {min(gray_flat)-1}|{r_i_count[min(gray_flat)-1]}, {min(gray_flat)}|{r_i_count[min(gray_flat)]}')
        logger.debug(f'MAX: {max(gray_flat)} --> {max(gray_flat)}|{r_i_count[max(gray_flat)]}, {max(gray_flat)+1}|{r_i_count[max(gray_flat)+1]}')
    except IndexError as e:
        logger.debug(e)

    # Step 2. Sum (cumulative)
    r_sum += np.arange(0,2**args.bits, dtype=np.uint64)*r_i_count
    r_cumsum = r_sum.cumsum()

    # Step 3. Create transformation function: map original pixel value to new pixel value
    s_i = r_cumsum * (2**args.bits-1) // (sum(gray_flat))
    logger.debug(f'range gray_flat: {min(gray_flat)} - {max(gray_flat)}')
    logger.debug(f'range s_i: {min(s_i)} - {max(s_i)}')
    if args.debug and not args.no_plot:
        plt_plot(r_i,s_i,title='transformation function', xlabel='r_i', ylabel='s_i')

    # Step 4. Apply transformation function
    gray_flat_hist_eq = np.zeros(gray_flat.shape, dtype=np.uint8)
    for ii,pixel in enumerate(gray_flat):
        gray_flat_hist_eq[ii] = s_i[np.where(r_i == pixel)]

    # Step 5.
    for pixel in gray_flat_hist_eq:
        s_i_count[pixel] += 1


    # Show images along with their respective histograms
    save_dir = args.image.rstrip('.tif')
    if args.local:
        save_dir += '/local'

    cv2.imwrite(f"{save_dir}/0.png",gray)

    image_out = gray_flat_hist_eq.reshape(gray.shape)
    logger.debug(image_out.shape)
    logger.debug(gray.shape)
    cv2.imwrite(f"{save_dir}/1.png",image_out)

    fig = plt_bar(r_i,r_i_count, title='histogram BEFORE equalization', xlabel='intensity value', ylabel='number of pixels')
    fig.savefig(f'{save_dir}/2.png')
    fig = plt_bar(r_i,s_i_count, title='histogram AFTER equalization', xlabel='intensity value', ylabel='number of pixels')
    fig.savefig(f'{save_dir}/3.png')

    return

if __name__ == '__main__':
    sys.exit(main())
