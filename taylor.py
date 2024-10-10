# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:45:30 2024

@author: joahb

this code uses the taylor series of sine to approximate sin(x) for a range of x values
"""

import numpy as np
import matplotlib.pyplot as plt

#all sine terms are zero because sin(0) = 0 so we only look at cosine terms and the coefficients for those are 1 or -1
def taylor_sin_using_cosine(x, n_terms):
    taylor_sum = 0
    for n in range(n_terms):
        # Each term alternates: (-1)^n * x^(2n+1) / (2n+1)!
        coeff = (-1)**n
        term = coeff * (x**(2*n + 1)) / np.math.factorial(2*n + 1)
        taylor_sum += term
    return taylor_sum

# Calculate sin(2) using Taylor series for 15 terms
x_single = 2
n_terms = 15
sin_approx_2 = taylor_sin_using_cosine(x_single, n_terms)
print(f"Taylor series approximation of sin(2) with {n_terms} terms: {sin_approx_2}")
print(f"Actual value of sin(2): {np.sin(2)}")

# Set up the x values from -10 to 10 in increments of 0.1
x_values = np.arange(-10, 10.1, 0.1)

# Calculate sin(x) using Taylor series for 15 terms
taylor_approximations = [taylor_sin_using_cosine(x, n_terms) for x in x_values]

# Plot the true sin(x) and its Taylor series approximation
plt.figure(figsize=(10, 6))
plt.plot(x_values, np.sin(x_values), label="sin(x)", color="blue")
plt.plot(x_values, taylor_approximations, label=f"Taylor Approximation with {n_terms} terms", linestyle="--", color="red")
plt.legend()
plt.title(f"Taylor Series Approximation of sin(x) with {n_terms} Terms")
plt.xlabel("x")
plt.ylabel("sin(x) and Approximation")
plt.grid(True)

# Save the plot to a file
plt.savefig("taylor.png")

plt.show()