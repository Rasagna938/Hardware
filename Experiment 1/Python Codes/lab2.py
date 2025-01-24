import numpy as np
import matplotlib.pyplot as plt

# Set a value for A
A = 2

# Define the grid for x and y
x = np.linspace(-3, 3, 500)
y = np.linspace(-3, 3, 500)
X, Y = np.meshgrid(x, y)

# Evaluate the equation
lhs = X**2 + Y**2 - np.sqrt(2) * X * Y
rhs = A**2 / 2

# Plot the contour
plt.figure(figsize=(8, 6))
plt.contour(X, Y, lhs, levels=[rhs], colors='blue')
plt.title(r"$x^2 + y^2 - \sqrt{2}xy = \frac{A^2}{2}$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.3)
plt.show()

