import sys
import pandas as pd
import numpy as np
    
    
def sum_norm(df):
    '''
    This function calculates the sum-normalized values (fractions) of the dataframe over columns
    '''
    n=df.shape[0]
    sumcol = df.sum(axis=0)
    sumcol.to_numpy
    rep_sum = np.tile(sumcol, (n,1))
    mat_norm = df/rep_sum
    return mat_norm


if __name__ == "__main__":
    sum_norm(sys.argv[1:])
