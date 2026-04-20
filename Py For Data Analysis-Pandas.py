import pandas as pd
import numpy as np

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)

frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])

frame2['debt'] = np.arange(6)

populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
               "Nevada": {2001: 2.4, 2002: 2.9}}

frame3 = pd.DataFrame(populations)


print(frame3.T)




"""
obj2 = pd.Series([5, -3, 10, 20], index=['a', 'b', 'c', 'd'])

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = pd.Series(sdata)

states = ["California", "Ohio", "Oregon", "Texas"]

obj4 = pd.Series(sdata, index=states)

obj4.name = 'population'
obj4.index.name = 'state'
"""