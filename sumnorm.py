import sys
import pandas as pd
import numpy as np
    
def sum_norm(df):
    '''
    This function calculates the sum-normalized values (fractions) of the dataframe over columns
    '''
    n = df.shape[0]
    sumcol = df.sum(axis=0)
    sumcol.to_numpy
    rep_sum = np.tile(sumcol, (n, 1))
    mat_norm = df/rep_sum
    return mat_norm


def scaling_range_norm(df, val_min=0, val_max=0):
    """
    This function calculates the scales-normalized values of the dataframe over columns
    """
    if val_min == 0 and val_max == 0:
        val_min = df.min()
        val_max = df.max()
    df_scaling = (df - val_min) / (val_max - val_min)

    return df_scaling

