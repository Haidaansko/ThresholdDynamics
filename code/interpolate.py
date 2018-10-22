#!/usr/bin/env python3

import csv
import numpy as np
import pandas as pd
import sys

from handler import grid_readval_csv


def interpolate(grid):
    return np.arange(5)


def main(argc, argv):
    if argc == 1:
        print(
            'Usage: ./interpolate.py <input filename>.csv [OPTIONAL] <ouput filename>.csv')
        sys.exit(1)

    grid = grid_readval_csv(argv[1])
    pd.DataFrame(interpolate(grid)).to_csv(argv[2])


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

