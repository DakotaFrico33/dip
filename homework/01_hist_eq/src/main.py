#!/usr/bin/env python3
import os
import sys

from numpy.lib.index_tricks import s_

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
    # Load image
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,args.image))
    original = cv2.imread(args.image)
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    gray_flat = gray.flatten()
    image_out_flat = np.zeros(gray_flat.shape, dtype=np.uint8)

    logger.debug(original.shape)
    logger.debug(gray.shape)
    logger.debug(gray_flat.shape)

    logger.debug(f'MIN: {min(gray_flat)}, MAX: {max(gray_flat)}, bits: {args.bits}, N: {2**args.bits}')
    if 2**args.bits < max(gray_flat):
        logger.error('incorrect number of bits')
        return

    # Step 1. Define range of intensities
    r_i = np.arange(0,2**args.bits, dtype=np.uint8)
    r_i_count = np.zeros(r_i.shape, dtype=np.uint64)
    s_i = np.zeros(r_i_count.shape, dtype=np.uint8)
    s_i_count = np.zeros(r_i.shape, dtype=np.uint64)

    # Step 2. Count occurences of pixels with same intensity value
    for pixel in gray_flat:
        r_i_count[pixel] += 1

    try:
        logger.debug(f'MIN: {min(gray_flat)} --> {min(gray_flat)-1}|{r_i_count[min(gray_flat)-1]}, {min(gray_flat)}|{r_i_count[min(gray_flat)]}')
        logger.debug(f'MAX: {max(gray_flat)} --> {max(gray_flat)}|{r_i_count[max(gray_flat)]}, {max(gray_flat)+1}|{r_i_count[max(gray_flat)+1]}')
    except IndexError as e:
        logger.debug(e)

    # Step 3. Calculate probability of occurrence for each intensity level
    p_r = r_i_count / sum(r_i_count)

    # Step 4. Cumulative sum
    r_cumsum = p_r.cumsum()

    # Step 5. Mapping of pixel intensities between the original image and the processed one
    s_i = r_cumsum * (2**args.bits-1)
    np.rint(s_i)

    logger.debug(f'range gray_flat: {min(gray_flat)} - {max(gray_flat)}')
    logger.debug(f'range s_i: {min(s_i)} - {max(s_i)}')
    if args.debug and not args.no_plot:
        plt_plot(r_i,s_i,title='transformation function', xlabel='r_i', ylabel='s_i')
        plt.show()

    # Apply transformation function
    for ii,pixel in enumerate(gray_flat):
        image_out_flat[ii] = s_i[np.where(r_i == pixel)]

    for pixel in image_out_flat:
        s_i_count[pixel] += 1

    # Save images and their respective histograms
    save_dir = args.image.rstrip('.tif')
    if args.local:
        save_dir += '/local'

    image_out = image_out_flat.reshape(gray.shape)
    logger.debug(image_out.shape)
    logger.debug(gray.shape)
    cv2.imwrite(f"{save_dir}/0.png",gray)
    cv2.imwrite(f"{save_dir}/1.png",image_out)

    fig = plt_bar(r_i,r_i_count, title='Histogram of original image', xlabel='intensity value', ylabel='number of pixels')
    fig.savefig(f'{save_dir}/2.png')
    fig = plt_bar(r_i,s_i_count, title='Histogram of processed image', xlabel='intensity value', ylabel='number of pixels')
    fig.savefig(f'{save_dir}/3.png')

    return

if __name__ == '__main__':
    sys.exit(main())
