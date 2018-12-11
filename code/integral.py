#!/usr/bin/env python3

import csv
import numpy as np
import pandas as pd
import sys
import interpolate as ip
from handler import grid_readval_csv


def rec_rule(grid, f):
    left = grid[:-1]
    right = grid[1:]
    f_v = np.vectorize(f, otypes=[float])
    return np.sum((right - left) * f_v((left + right) / 2))


def trap_rule(grid, f):
    if f is not None:
        left = grid[:-1]
        right = grid[1:]
        f_v = np.vectorize(f, otypes=[float])
        return np.sum((right - left) * (f_v(left) + f_v(right)) / 2)
    else:
        return np.sum((grid[0, 1:] - grid[0, :-1]) * (grid[1, 1:] + grid[1, :-1]) / 2)


def integrate(grid, f=None, method='trap'):
    # return np.sum(grid[1]) / (grid[0, -1] - grid[0, 0]) * grid.shape[1]
    if method == 'trap':
        return trap_rule(grid, f)
    if method == 'rec':
        return rec_rule(grid, f)

    
def main(argc, argv):
    if argc == 1:
        print('Usage: ./interpolate.py <input filename>.csv <output filename>.csv')
        sys.exit(1)

    grid = grid_readval_csv(argv[1])
    poly = ip.interpolate(integrate(grid))
    pd.DataFrame(poly).to_csv(argv[2])


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

