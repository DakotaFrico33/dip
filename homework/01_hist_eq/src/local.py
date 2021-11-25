#!/usr/bin/env python3
import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np

from arg_parse import args
from logger_setup import logger
from histogram_equalization import transformation

os.environ['DISPLAY'] = ':0'

def main():
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,args.image))
    original = cv2.imread(args.image, 0)

    k = args.kernel_size//2
    image_in = np.pad(original, (k, k), 'constant', constant_values=(0))

    rows = image_in.shape[0]-k
    cols = image_in.shape[1]-k
    c = []
    for i in range (k,rows):
        for j in range (k,cols):
            section = image_in[i-k:i+k+1,j-k:j+k+1]
            section_transformed = transformation(section,args)
            mid = section_transformed[k,k]
            c.append(mid)
        logger.info(f"{i} of {rows}")

    image_out = np.array(c,dtype=np.uint8)
    image_out = image_out.reshape(original.shape)

    if args.save:
        save_dir = args.image.split('.tif')[0]
        save_dir += '/local'

        cv2.imwrite(f"{save_dir}/0.png",image_in)
        cv2.imwrite(f"{save_dir}/{args.kernel_size}.png",image_out)

    if args.show:
        cv2.imshow("image_in",image_in)
        cv2.waitKey(0)

        cv2.imshow("out",image_out)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    sys.exit(main())
