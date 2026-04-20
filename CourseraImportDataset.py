import pandas as pd
import numpy as np

file_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

df = pd.read_csv(file_path)

#print(df.tail(10))

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

#print("headers\n", headers)

df.columns = headers
#print(df.columns)
#print(df.head(10))

df1 = df.replace('?', np.nan)
df = df1.dropna(subset=["price"], axis=0)

#print(df.head(20))

#df.to_csv("automobile.csv", index=False)

#print(df.columns)
print(df[['length', 'compression-ratio']].describe())