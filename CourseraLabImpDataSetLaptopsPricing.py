import pandas as pd
import numpy as np

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"

df = pd.read_csv(file_path)

columns = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]

df.columns = columns

df.replace('?', np.nan, inplace=True)

#print(df.describe(include='all'))

print(df.info())