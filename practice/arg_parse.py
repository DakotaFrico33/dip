#!/usr/bin/env python3
import argparse
import sys

#######################  parser  ###########################################
class ArgParse(object):
    def __init__(self, args):
        self._args = self._parse_args(args)

    @property
    def args(self):
        return self._args

    def _parse_args(self, args):
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument('--debug', action='store_true', help='turn on logging.debug. [Default: logging.info]')
        self._parser.add_argument('--image', '-i', default='./img/lena_color_256.tif', help="path to input image [Default: ./img/lena.tif]")
        self._parser.add_argument('--kernel-sizes', type=int, default=[3,9,15], nargs='*', help='set kenel sizes. (i.e. -k 3 5 11)',)
        self._parser.add_argument('--blurred','-b', action='store_false', help='turn off average blur [Default: ON]')
        self._parser.add_argument('--gaussian','-g', action='store_false', help='turn off gaussian blur [Default: ON]')
        self._parser.add_argument('--median','-m', action='store_false', help='turn off median blur [Default: ON]')
        self._parser.add_argument('--bilateral', type=int, default=11, help='define bilateral filter diameter value [Default: 11]')
        self._parser.add_argument('--offset','-o', type=int, default=1, help='define offset for keyboard control. [Default: 1] Works with *2.py')
        self._parser.add_argument('--width','-w', type=int, default=256, help='define width of resized picture')
        self._parser.add_argument('--video', '-v', default='./my_img/glass_swirl2.mp4', help="path to input video [Default: ./my_img/glass_swirl2.mp4]")
        self._parser.add_argument('--loop', action='store_true', help='turn on looping thorugh video [Default: OFF]')
        return self._parser.parse_args(args)


#######################  parser call  #######################################
args = ArgParse(args = sys.argv[1:]).args
print(args)
