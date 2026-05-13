import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])

#plt.scatter(x, y)
#plt.show()

coefficients = np.polyfit(x, y, 3)
poly_func = np.poly1d(coefficients)

x_curve = np.linspace(min(x), max(x), 100)
y_curve = poly_func(x_curve)

plt.scatter(x, y, label='Original Data')
plt.plot(x_curve, y_curve, color='red', label='Fitted Poly')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Polynomial Fit Example')
plt.legend()
plt.show()