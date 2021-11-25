#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

from logger_setup import logger



def transformation(gray, args):
    gray_flat = gray.flatten()
    image_out_flat = np.empty(gray_flat.shape, dtype=np.uint8)

   # Step 1. Define range of intensities
    r_i = np.arange(0,2**args.bits, dtype=np.uint8)
    r_i_count = np.zeros(r_i.shape, dtype=np.uint64)
    s_i = np.zeros(r_i.shape, dtype=np.uint8)

    # Step 2. Count occurences of pixels with same intensity value
    for pixel in gray_flat:
        r_i_count[pixel] += 1

    # Step 3. Calculate probability of occurrence for each intensity level
    p_r = r_i_count / sum(r_i_count)

    # Step 4. Cumulative sum
    r_cumsum = p_r.cumsum()

    # Step 5. Mapping of pixel intensities between the original image and the processed one
    s_i = r_cumsum * (2**args.bits-1)
    s_i = np.floor(s_i)

    # Apply transformation function
    for ii,pixel in enumerate(gray_flat):
        image_out_flat[ii] = s_i[np.where(r_i == pixel)]

    s_i_count = np.zeros(r_i.shape, dtype=np.uint64)
    for pixel in image_out_flat:
        s_i_count[pixel] += 1

    image_out = image_out_flat.reshape(gray.shape)

    # Save/show plots
    if args.kernel_size == -1:
        if args.save:
            save_dir = args.image.split('.tif')[0]
            logger.info(save_dir)

        fig = plt_bar(r_i,r_i_count, title='Histogram of original image', xlabel='intensity value', ylabel='number of pixels')
        if args.save:
            fig.savefig(f'{save_dir}/2.png')
        if args.show:
            plt.show()

        fig = plt_bar(r_i,s_i_count, title='Histogram of processed image', xlabel='intensity value', ylabel='number of pixels')
        if args.save:
            fig.savefig(f'{save_dir}/3.png')
        if args.show:
            plt.show()

        if args.save:
            fig = plt_plot(r_i,s_i,title='Transformation function', xlabel='r_i', ylabel='s_i')
            fig.savefig(f'{save_dir}/4.png')
        if args.show:
            plt.show()

    return image_out


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
