#!/usr/bin/env python3

import csv
import numpy as np
import pandas as pd
import sys

from handler import grid_readval_csv


def TDMA(A, B, C, F):
    '''
    A: shape = (n,), A[0] == 0
    B: shape == (n,), B[-1] == 0
    C: shape == (n,)
    F: shape == (n,)
    '''
    n = C.size
    p = np.zeros(n)
    q = np.zeros(n)
    x = np.zeros(n)
    for i in range(C.size - 1):
        p[i + 1] = -B[i] / (A[i] * p[i] + C[i])
        q[i + 1] = (F[i] - A[i] * q[i]) / (A[i] * p[i] + C[i])
    x[n - 1] = (F[n - 1] - A[n - 1] * q[n - 1]) / (A[n - 1] * p[n - 1] + C[n - 1])
    for i in range(n - 1):
        x[n - 2 - i] = x[n - 1 - i] * p[n - 1 - i] + q[n - 1 - i]
    return x


def make_spline(grid):
    a, b, c, d = None, None, None, None
    a = grid[1, 1:]
    h = np.diff(grid[0])
    A = np.zeros(h.size - 1)
    A[1:] = h[1:-1]
    B = np.zeros(h.size - 1)
    B[:-1] = h[1:-1]
    C = 2 * (h[:-1] + h[1:])
    F = 3 * ((grid[1, 2:] - grid[1, 1:-1]) / h[1:] - (grid[1, 1:-1] - grid[1, :-2]) / h[:-1])
    c = np.zeros(h.size + 1)
    res = TDMA(A, B, C, F)
    c[1:-1] = res
    d = (c[1:] - c[:-1]) / (3 * h)
    b = (grid[1, 1:] - grid[1, :-1]) / h + h * (c[:-1] + 2 * c[1:]) / 3
    spline = { 'x': grid[0], 0 : a, 1 : b, 2 : c[1:], 3 : d }
    return spline


def spline_calc(spline, t, derivative=0):
    x = spline['x']
    if t < x[0] or t > x[-1]:
        return np.nan
    i = (x < t).sum()
    h = t - x[i]
    if derivative == 1:
        return spline[1][i - 1] + 2 * h * spline[2][i - 1] + 3 * h**2 * spline[3][i - 1]
    elif derivative == 2:
        return 2 * spline[2][i - 1] + 6 * h * spline[3][i - 1]
    return sum(h ** j * spline[j][i - 1] for j in range(4))


def interpolate(grid):
    return make_spline(grid)


def main(argc, argv):
    if argc == 1:
        print(
            'Usage: ./interpolate.py <input filename>.csv [OPTIONAL] <ouput filename>.csv')
        sys.exit(1)

    grid = grid_readval_csv(argv[1])
    pd.DataFrame(interpolate(grid)).to_csv(argv[2])


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

