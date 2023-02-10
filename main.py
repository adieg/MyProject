import sys
import normData as nm
import pandas as pd
import numpy as np

data = {
  "V1": [50, 55, 10],
  "V2": [10, 45, 45]
}

def main(df, normalization_type="scaling_range"):
    """
    This function send calculation to the right normalization type:
    """
    if normalization_type == "sum":
        result = nm.sum_norm(df)
    elif normalization_type == "scaling_range":
        result = nm.scaling_range_norm(df)
    else:
        print("Error in normalization type! Calculating sum normalization.")
        result = nm.sum_norm(df)

    return result


if __name__ == "__main__":

    df = pd.DataFrame(data)

    print(main(df, sys.argv[1:]))
