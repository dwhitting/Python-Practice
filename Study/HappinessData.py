import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/Users/drewwhitting/Documents/VSCodePython/HappinessDataKaggle/2019.csv', index_col=0)

cGenerosity = data['Generosity']
cScore = data['Score']

"""
plt.scatter(cGenerosity, cScore)
plt.xlabel('Generosity')
plt.ylabel('Happiness Score')
plt.title('Country Population Showing Generosty vs Happiness Score')
plt.show()
"""
plt.hist(cGenerosity, bins=25)
plt.xlabel('Generosity')
plt.title('Histogram of Country Population Happiness Score')
plt.show()

#Note

"""
x = [5, 6, 7, 8]
y = [3, 1, 8, 4]

plt.scatter(x, y)
plt.show()

Index(['Overall rank', 'Country or region', 'Score', 'GDP per capita',
       'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption'],
      dtype='object')

                   Country or region  Score  GDP per capita  ...  Freedom to make life choices  Generosity  Perceptions of corruption
Overall rank                                           ...                                                                     
1                      Finland  7.769           1.340  ...                         0.596       0.153                      0.393
2                      Denmark  7.600           1.383  ...                         0.592       0.252                      0.410
3                       Norway  7.554           1.488  ...                         0.603       0.271                      0.341
4                      Iceland  7.494           1.380  ...                         0.591       0.354                      0.118
5                  Netherlands  7.488           1.396  ...                         0.557       0.322                      0.298


"""