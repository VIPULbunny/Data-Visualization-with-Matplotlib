# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Example 1: Basic scatter plot
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 10, 20, 30, 40])
plt.plot(x, y, 'o')  # Plot with circular markers
plt.title("Basic Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Example 2: Custom marker styles
plt.plot(y, marker='*', ms=10, mec='r', mfc='y')  # Star markers
plt.title("Custom Marker Styles")
plt.show()

# Example 3: Line styles and colors
plt.plot(y, ls='dotted', color='y', linewidth=5)
plt.title("Dotted Line with Custom Color")
plt.show()

# Example 4: Overlapping plots with different colors
plt.plot(x, color='r', label='Red Line')
plt.plot(y, color='g', label='Green Line')
plt.title("Overlapping Plots")
plt.legend()
plt.show()

# Example 5: Subplots (2 rows, 1 column)
x1 = [1, 2, 3, 4, 5, 6]
y1 = [10, 20, 30, 40, 50, 60]
x2 = [3, 8, 1, 10]
y2 = [6, 2, 7, 11]

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title("Plot 1")

plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.title("Plot 2")

plt.suptitle("Two Subplots (2x1)")
plt.show()

# Example 6: Subplots (2 rows, 3 columns)
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.plot(x1, y1)
    plt.title(f"Plot {i}")
plt.suptitle("Grid of Subplots (2x3)")
plt.show()

# Example 7: Custom Axes
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Custom axes position
ax.plot(x2, y2)
ax.set_title("Custom Axes")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
plt.show()
