import pandas as pd
import numpy as np

df = pd.DataFrame({"key1": ["a", "a", None, "b", "b", "a", None],
                   "key2" : pd.Series([1, 2, 1, 2,1, None, 1], dtype='Int64'),
                   "data1": np.random.standard_normal(7),
                   "data2": np.random.standard_normal(7)})

grouped = df["data1"].groupby(df["key1"])

means = df["data1"].groupby([df["key1"], df["key2"]]).mean()

print(df.groupby(["key1"]).count())