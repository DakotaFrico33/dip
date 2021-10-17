#!/usr/bin/env python3
# adapted from: https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/
import os
import sys

import cv2
import imutils
import numpy as np

from arg_parse import args
from logger_setup import logger
from open_cv import put_text, read_key


###################################################################3
def main():
    video = args.video
    cwd = os.getcwd()
    assert os.path.exists(os.path.join(cwd,video))
    source = cv2.VideoCapture(args.video)

    while True:
        ret, img = source.read()
        if not ret:
           logger.info('Video ended. Restart video...')
           if args.loop:
               source.set(cv2.CAP_PROP_POS_FRAMES, 0)
               continue
               # _, img = source.read()
           else:
               logger.info('Video ended. Exit immediately!')
               break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized = imutils.resize(gray, width=args.width)
        a=resized
        h_stack=[a]

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        resized = imutils.resize(blurred, width=args.width)
        c=resized
        h_stack.append(c)

        wide = cv2.Canny(blurred, 10, 200)
        resized = imutils.resize(wide, width=args.width)
        c=resized
        h_stack.append(c)


        cv2.imshow("Live", np.hstack(h_stack))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info('Pressed Q button. Exit immediately!')
            break

    cv2.destroyAllWindows()
    source.release()

if __name__ == '__main__':
    sys.exit(main())
