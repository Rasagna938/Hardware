import numpy as np
import matplotlib.pyplot as plt

# Define the range for t
t = np.linspace(-10, 10, 500)

# Define x(t) and y(t)
x = t
y = t

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(t, y, label=r"$y(t) = x(t)$")
plt.title(r"$y(t) = x(t)$")
plt.xlabel("t")
plt.ylabel("y(t), x(t)")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.3)
plt.legend()
plt.show()

