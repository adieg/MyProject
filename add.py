import sumnorm
import pandas as pd
import numpy as np

data = {
    "V1": [30, 50, 20],
    "V2": [10, 45, 45]
}

df1 = pd.DataFrame(data)

print(sumnorm.sum_norm(df1))