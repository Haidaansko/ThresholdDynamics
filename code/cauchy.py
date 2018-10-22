#!/usr/bin/env python3

import json
import numpy as np
import pandas as pd
import derivative
import handler
import integral
import interpolate
import sys


def f(x, z, S, beta):
    return beta * (x - z)


def solve(grids, params):
    return np.random.randint(0, 5, size=(2, 5))


def main(argc, argv):
    if argc < 5:
        print('Usage: ./cauchy.py <param filename>.json <grid fname>.csv <grid fname>.csv <grid fname>.csv <output>.csv')
        sys.exit(1)

    params = dict()
    with open(argv[1]) as json_file:
        params = json.load(json_file)
        if 'T' not in params \
                or 'x0' not in params \
                or 'y0' not in params \
                or 'beta' not in params:
            print('Parameters T, x0, y0, beta are expected')
            sys.exit(1)

    U = handler.grid_readval_csv(argv[2])
    z = handler.grid_readval_csv(argv[3])
    rho = handler.grid_readval_csv(argv[4])

    result = solve((U, z, rho), params)
    pd.DataFrame(result).to_csv(argv[5])


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)

