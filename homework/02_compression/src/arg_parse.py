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
        self._parser.add_argument('--show', action='store_true', default=False, help='show openCV images. [Default: False]',)
        self._parser.add_argument('--save', action='store_true', default=False, help='save images to dedicated folder. [Default: False]',)
        self._parser.add_argument('--image', '-i', default='./../images/lena.tif', help="path to input image [Default: ./../images/lena.tif]")
        self._parser.add_argument('--block-size','-b', type=int, default=2, help='set size of DCT squared block. [Default: 2]',)
        return self._parser.parse_args(args)


#######################  parser call  #######################################
args = ArgParse(args = sys.argv[1:]).args
print(args)
