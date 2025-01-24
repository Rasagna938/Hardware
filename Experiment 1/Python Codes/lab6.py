import numpy as np
import matplotlib.pyplot as plt

# Define the range for x
x = np.linspace(-10, 10, 500)

# Define y = -x
y = -x

# Plot the line
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$y = -x$")
plt.title("Plot of $y = -x$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.3)
plt.legend()
plt.show()

