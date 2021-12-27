#!/usr/bin/env python3
import os
import sys
from math import cos, pi, sqrt

from logger_setup import logger


def idct_2d_calculator(val, block_size=2):
    coeff = (sqrt(1/block_size), sqrt(2/block_size))
    C_j = coeff[0] if x==0 else coeff[1]
    C_k = coeff[0] if y==0 else coeff[1]
    sum = 0
    for j,row in enumerate(block):
        for k,num in enumerate(row):
            sum += C_j * C_k * num * cos(((2*x+1)*j*pi)/(2*block_size)) * cos(((2*y+1)*k*pi)/(2*block_size))

    f = 2/block_size * sum
    return f


def main():
    val_in = int(input("Enter your value: "))
    val_out = idct_2d_calculator(val_in)
    print(val_out)
    return

if __name__ == '__main__':
    sys.exit(main())
