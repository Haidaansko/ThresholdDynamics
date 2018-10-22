#!/usr/bin/env python3

import csv
import numpy as np
import pandas as pd
import sys
import interpolate as ip
from handler import grid_readval_csv


def integrate(grid):
    return np.sum(grid[1]) / (grid[0, -1] - grid[0, 0]) * grid.shape[1]


def main(argc, argv):
    if argc == 1:
        print('Usage: ./interpolate.py <input filename>.csv <output filename>.csv')
        sys.exit(1)

    grid = grid_readval_csv(argv[1])
    poly = ip.interpolate(integrate(grid))
    pd.DataFrame(poly).to_csv(argv[2])


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

