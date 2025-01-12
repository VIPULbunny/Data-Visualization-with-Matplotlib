# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Example 1: Scatter Plot
x = [5, 6, 7, 3, 4, 73, 46, 65, 2, 4, 76, 45, 34, 56, 34, 66]
y = [45, 34, 56, 36, 74, 2, 36, 75, 35, 53, 65, 74, 74, 2, 45, 65]
plt.scatter(x, y, color='red', s=100, alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Example 2: Bar Plot
x = ['One', 'Two', 'Three', 'Four']
y = [6, 9, 1, 20]
plt.bar(x, y, width=0.5, color='blue')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Example 3: Horizontal Bar Plot
plt.barh(x, y, height=0.5, color='green')
plt.title("Horizontal Bar Plot")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()

# Example 4: Histogram
x = np.random.normal(200, 10, 300)  # Generate random data
plt.hist(x, bins=10, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# Example 5: Pie Chart
x = [25, 30, 25, 20]
labels = ["Chocolate", "Vanilla", "Plain", "Strawberry"]
plt.pie(x, labels=labels, startangle=90, explode=[0.2, 0, 0, 0], shadow=True, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
