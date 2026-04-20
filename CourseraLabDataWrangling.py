import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt

file_path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(file_path, names=headers)

df.replace("?", np.nan, inplace=True)

missing_data = df.isnull()

"""
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
"""

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses: ", avg_norm_loss)

df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

avg_bore = df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

df["bore"].replace(np.nan, avg_bore, inplace=True)

avg_stroke = df["stroke"].astype("float").mean(axis=0)
print(avg_stroke)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype("float").mean(axis=0)
print(avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
print(avg_peakrpm)
df.replace(np.nan, avg_peakrpm, inplace=True)

num_doors_cnts = df['num-of-doors'].value_counts()
num_doors_indxmax = df["num-of-doors"].value_counts().idxmax()
print(num_doors_indxmax) #shows max of that index

df['num-of-doors'].replace(np.nan, 'four', inplace=True)

df.dropna(subset=['price'], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

df[['bore', 'stroke']] = df[['bore', 'stroke']].astype('float')
df[['normalized-losses', 'horsepower']] = df[['normalized-losses', 'horsepower']].astype('int')
df[['price']] = df[['price']].astype('float')
df[['peak-rpm']] = df[['peak-rpm']].astype('float')

df['city-L/100km'] = 235/df['city-mpg']

df['highway-L/100km'] = 235/df['highway-mpg']


df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()

print(df[['length', 'width', 'height']].head())

#plt.hist(df['horsepower'])
#plt.xlabel('horsepower')
#plt.ylabel('count')
#plt.title('horsepower bins')

bins = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)

group_names = ['low', 'medium', 'high']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)


print(df[['horsepower', 'horsepower-binned']].head(20))

print(df['horsepower-binned'].value_counts())

#plt.bar(group_names, df['horsepower-binned'].value_counts())
#plt.xlabel('horsepower')
#plt.ylabel('count')
#plt.title('horsepower bins')


dummy_variables_1 = pd.get_dummies(df['fuel-type'])

dummy_variables_1.rename(columns={'gas': 'fuel-type-gas', 'diesel' : 'fuel-type-diesel'}, inplace=True)
df = pd.concat([df, dummy_variables_1], axis=1)
df.drop("fuel-type", axis=1, inplace=True)

if dummy_variables_1.items() == True:
    dummy_variables_1 == '1'


print(dummy_variables_1.head(20))