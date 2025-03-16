from scipy.optimize import minimize
import numpy as np

# Function to minimize
def func(x):
    return (x - 3) ** 2 + 4

# Finding the minimum
result = minimize(func, x0=np.array([0]))  # Initial guess at x=0

# Formatting the output to 2 decimal places
print("Optimal value of x: {:.2f}".format(result.x[0]))
print("Minimum function value: {:.2f}".format(result.fun))
