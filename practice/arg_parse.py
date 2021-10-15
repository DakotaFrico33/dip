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
        self._parser.add_argument('--debug', action='store_true', help='turn on logging.debug. Default: logging.info')
        self._parser.add_argument('--app', help='name of app on heroku')
        self._parser.add_argument('--port', help='heroku port', type=int, default=5000)

        return self._parser.parse_args(args)


#######################  parser call  #######################################
args = ArgParse(args = sys.argv[1:]).args
print(args)
