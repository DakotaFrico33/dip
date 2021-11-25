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
    img = cv2.imread(args.image,0)
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(3,3))
    cl1 = clahe.apply(img)
    cv2.imshow("gray",img)
    cv2.waitKey(0)
    cv2.imshow('clahe_2.jpg',cl1)
    cv2.waitKey(0)
    cv2.imwrite('clahe_2.jpg',cl1)
    return
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,args.image))
    gray = cv2.imread(args.image, 0)
    # gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    a = gray
    image_out = np.empty(a.shape, dtype=np.uint8)
    c = []
    k = args.kernel_size//2
    if not args.no_pad:
        b = np.pad(a, (k, k), 'constant', constant_values=(0))

    for i in range (k,b.shape[0]-k):
        for j in range (k,b.shape[1]-k):
            section = b[i-k:i+k+1,j-k:j+k+1]
            # logger.debug(section)

            section_transformed = transformation(section,args)
            section_transformed = section_transformed.flatten().tolist()
            # print(section_transformed.flatten())
            # c[i-k,j-k] = section_transformed.flatten()
            # print (section)
            # logger.debug(section_transformed)
            # print(section_transformed[(k+1)//2,(k+1)//2])
            # c[i-k][j-k] = section_transformed[((k*k)+1)//2]
            mid = section_transformed[((k*k)+1)//2]
            c.append(mid)
            # logger.info(f'running {i},{j}')
        logger.debug(f"{i},{j}")
        # logger.debug(section.flatten().tolist())
        # logger.debug(section_transformed)

    image_out = np.array(c,dtype=np.uint8)
    image_out = image_out.reshape(a.shape)

    cv2.imshow("gray",a)
    cv2.waitKey(0)

    cv2.imshow("out.png",image_out)
    cv2.waitKey(0)

    return

if __name__ == '__main__':
    sys.exit(main())
