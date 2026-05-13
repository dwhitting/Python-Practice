import pandas as pd
import numpy as np

float_data = pd.Series([1.2, -3.5, np.nan, 0])

string_data = pd.Series(['aardvark', np.nan, None, 'avocado'])

float_data = pd.Series([1, 2, None], dtype='float')

#print(float_data.isna())

#Filering

data = pd.Series([1, np.nan, 3.5, np.nan, 7])

data= pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],
                   [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])

data[4] = np.nan

data.dropna(axis="columns", how="all", inplace=True)

df = pd.DataFrame(np.random.standard_normal((10, 5)))

df.iloc[:6, 1] = np.nan
df.iloc[:2, 2] = np.nan
df.iloc[2:6, 4] = np.nan

print(df[0].fillna(df.mean()))