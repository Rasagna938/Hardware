import numpy as np
import matplotlib.pyplot as plt

# Set the value of A
A = 5

# Define the angle range for the circle
theta = np.linspace(0, 2 * np.pi, 500)

# Parametric equations for the circle
x = np.sqrt(A) * np.cos(theta)
y = np.sqrt(A) * np.sin(theta)

# Plot the circle
plt.figure(figsize=(8, 8))
plt.plot(x, y, label=r"$x^2 + y^2 = A$")
plt.title(r"$x^2 + y^2 = A$ (A = 5)")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.axis("equal")  # Ensure the circle looks round
plt.grid(alpha=0.3)
plt.legend()
plt.show()

