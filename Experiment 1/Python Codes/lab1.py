import numpy as np
import matplotlib.pyplot as plt

# Set a value for A
A = 2

# Define the x range
x = np.linspace(-2, 2, 500)  # Adjust range and points for better visualization

# Compute y^2 and then take the square root
y_squared = 4 * x**2 - (4 * x**4) / A**2
y_squared = np.maximum(y_squared, 0)  # Ensure no negative values inside the square root
y_positive = np.sqrt(y_squared)
y_negative = -y_positive

# Plot the curve
plt.figure(figsize=(8, 6))
plt.plot(x, y_positive, label="Upper Branch")
plt.plot(x, y_negative, label="Lower Branch")
plt.title(r"$y^2 = 4x^2 - \frac{4x^4}{A^2}$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.3)
plt.legend()
plt.show()

