import numpy as np
import matplotlib.pyplot as plt

x = range (0, 9)
y = (25, 33, 41, 53, 59, 70, 78, 86, 98)

plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.plot(x, p(x), 'g-')
#plt.show()

print(np.poly1d(p(6)))