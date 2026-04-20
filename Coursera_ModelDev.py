import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

file_path= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"

df = pd.read_csv(file_path)


"""
lm = LinearRegression()
X = df[['engine-size']]
Y = df['price']

#lm.fit(X, Y)

#Yhat=lm.predict(X)
#print(lm.coef_)
"""
Z = df[['normalized-losses', 'highway-mpg']]
"""
lm.fit(Z, df['price'])

print(lm.intercept_)
print(lm.coef_)

width = 12
height = 10
#plt.figure(figsize=(width, height))
#sns.regplot(x='peak-rpm', y='price', data=df)
#sns.residplot(x=df['highway-mpg'], y=df['price'])
#plt.ylim(0,)
#plt.show()

#print(df[['peak-rpm', 'highway-mpg', 'price']].corr())

Y_hat = lm.predict(Z)
plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()


def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()


x = df['highway-mpg']
y = df['price']

f = np.polyfit(x, y, 11)
p = np.poly1d(f)
print(p)
   
PlotPolly(p, x, y, 'highway-mpg')
np.polyfit(x, y, 3)
"""

from sklearn.preprocessing import PolynomialFeatures

pr=PolynomialFeatures(degree=2)
Z_pr = pr.fit_transform(Z)
print(Z_pr.shape)

y = df['price']

X = df['engine-size']
Y = df['price']

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]

pipe=Pipeline(Input)

Z = Z.astype(float)
pipe.fit(Z, y)
ypipe=pipe.predict(Z)
ypipe[0:4]

lm = LinearRegression
lm.fit(X,Y)
print('The R-square is: ', lm.score(X, Y))

