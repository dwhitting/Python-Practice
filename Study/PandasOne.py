import pandas as pd

"""
df = pd.read_csv('/Users/drewwhitting/Documents/' \
                 'VSCodePython/data.csv')
print(df.head())
"""

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 
                 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df.iloc[3, 1])