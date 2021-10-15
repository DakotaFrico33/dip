#!/usr/bin/env python3
import logging

from arg_parse import args


if not args.debug:
    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
else:
    FORMAT = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ]\n\t%(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

logger = logging.getLogger(__name__)
