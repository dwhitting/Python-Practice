import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/20240522154643/auto-mpg%5B1%5D.csv')

sns.regplot(x='mpg',
            y='acceleration',
            data=df)

#plt.show()

titanic_df = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/20240903112658/train.csv')

sns.regplot(x='Fare',
            y='Age',
            data=titanic_df,
            color='b',)
plt.show()

#datasets are build into seaborn
#titanic = sns.load_dataset("mpg")
#print(titanic.head())
