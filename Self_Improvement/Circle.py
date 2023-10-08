import matplotlib.pyplot as plt
import numpy as np

# Create an array of angles to generate points on the circle
theta = np.linspace(0, 2 * np.pi, 1000)

# Define the radius of the circle
radius = 1.0

# Calculate the x and y coordinates of the points on the circle
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Plot the circle
plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')  # Ensure the aspect ratio is equal

# Display the plot
plt.show()
