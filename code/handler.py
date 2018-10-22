#!/usr/bin/env python3

import pandas as pd
import sys


def grid_readval_csv(fname):
    try:
        grid = pd.read_csv(fname).values
    except Exception as e:
        print(str(e))
        sys.exit(1)
    return grid

