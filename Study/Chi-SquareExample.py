import pandas as pd
from scipy.stats import chi2_contingency

data = [[20, 30],  #Male: [Like, Dislike]
        [25, 25]]  #Femail: [Like, Dislike]

df = pd.DataFrame(data, columns=["Like", "Dislike"], index=['Male', 'Female'])

chi2, p, dof, expected = chi2_contingency(df)

print('Chi-square Statistic: ', chi2)
print('Deg of Freedon: ', dof)
print('P-value: ', p)
print('Expected Freq: \n', expected)
