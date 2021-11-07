#!/usr/bin/env python3
# from: https://photo.stackexchange.com/questions/40401/what-does-frequency-mean-in-an-image
import os

import imageio
from PIL import Image
from numpy.fft import rfft2, irfft2
import numpy as np

from arg_parse import args

def save_dims(ft, low, high, name):
    print(low, high, name)
    ft2 = np.zeros_like(ft)
    # copy the frequencies from low to high but all others stay zero.
    ft2[low:high, low:high] = ft[low:high, low:high]
    save(ft2, name)

def save(ft, name):
    rft = irfft2(ft)
    img = Image.fromarray(rft)
    img = img.convert('L')
    img.save(name)

def main():
    # Convert input into grayscale and save.
    img = Image.open(f"{args.folder}/input.jpg")
    img = img.convert('L')
    img.save(f"{args.folder}/input_gray.png")
    # Do Fourier Transform on image.
    ft = rfft2(img)
    # Take only zeroth frequency and do Inverse FT and save.
    save_dims(ft, 0, 1, f'{args.folder}/output_0.png')
    # Take first two frequencies in both directions.
    save_dims(ft, 0, 2, f'{args.folder}/output_1.png')
    save_dims(ft, 0, 3, f'{args.folder}/output_2.png')
    # Take first 50% of frequencies.
    x = min(ft.shape)
    save_dims(ft, 0, x//2, f'{args.folder}/output_50p.png')

def generateGif():
    ''' Generates images to be later converted to a gif.
    This requires ImageMagick:
    convert -delay 100 -loop 0 output_*.png animation.gif
    '''
    if not os.path.exists(f'{args.folder}/animation/'):
        os.makedirs(f'{args.folder}/animation/')

    img = Image.open(f'{args.folder}/input.jpg')
    img = img.convert('L')
    # Resize image before any calculation.
    size = (640,480)
    img.thumbnail(size, Image.LANCZOS)
    ft = rfft2(img)

    fnames = []
    for x in range(0, max(ft.shape)):
        ft2 = np.zeros_like(ft)
        ft2[0:x, 0:x] = ft[0:x,0:x]
        rft = irfft2(ft2)
        img_out = Image.fromarray(rft).convert('L')
        fname = f'{args.folder}/animation/output_{(x, )}.jpg'
        fnames.append(fname)
        img_out.save(fname, quality=60, optimize=True)

    if args.mode == 'default':
        images = []
        for fname in fnames:
            images.append(imageio.imread(fname))
        imageio.mimsave(f'{args.folder}/animation.gif', images)


    if args.mode == 'I':
        with imageio.get_writer(f'{args.folder}/animation.gif', mode='I', duration=0.2) as writer:
            for fname in fnames:
                image = imageio.imread(fname)
                writer.append_data(image)


if __name__=='__main__':
    main()
    generateGif()
