import numpy as np
import matplotlib.pyplot as plt

# Define the function
def parabola(x):
    return 2.5 * (1 - (x / 5) ** 2)

# Generate x values
x = np.linspace(-5, 5, 500)

# Calculate y values
y = parabola(x)

# Plot the parabola
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Y = 2.5 * (1 - (x/5)^2)", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Add y-axis
plt.title("Parabola: Y = 2.5 * (1 - (x/5)^2)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
