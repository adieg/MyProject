
def sum_norm(df):
    import pandas as pd
    import numpy as np
    n=df.shape[0]
    sumcol = df.sum(axis=0)
    sumcol.to_numpy
    rep_sum = np.tile(sumcol, (n,1))
    mat_norm = df/rep_sum
    return mat_norm