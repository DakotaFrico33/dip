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
        self._parser.add_argument('--folder', '-f', default='01', help="path to folder of input image [Default: 01]")
        self._parser.add_argument('--mode', '-m', default='default', help="mode")
        return self._parser.parse_args(args)


#######################  parser call  #######################################
args = ArgParse(args = sys.argv[1:]).args
print(args)
