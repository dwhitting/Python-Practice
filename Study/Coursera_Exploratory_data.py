import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

filepath="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"

df = pd.read_csv(filepath, header=0)

df_gptest = df[['GPU', 'CPU_core', 'Price']]
grouped_test = df_gptest.groupby(['GPU', 'CPU_core'], as_index=False).mean()
print(grouped_test)


"""
sns.regplot(x='Weight_pounds', y='Price', data=df)
plt.ylim(0,)
plt.show()

sns.boxenplot(x="Storage_GB_SSD", y='Price', data=df)
plt.show()


for param in ['CPU_frequency', 'Screen_Size_inch', 
              'Weight_pounds']: 
        print(f"Correlation of Price and {param} is",
                df[[param,"Price"]].corr())




print(df.describe(include=['object']))
    
"""