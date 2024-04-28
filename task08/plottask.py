# plottask.py
# a program that outputs a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
# author : Nataliia Dragunova + Gpt chat

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 values from a normal distribution with mean 5 and standard deviation 2
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Plot the histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='blue', label='Normal Distribution')

# Define the function h(x) = x^3
def h(x):
    return x**3

# Generate x values from 0 to 10
x_values = np.linspace(0, 10, 100)
# Evaluate h(x) for each x
y_values = h(x_values)

# Plot the function h(x) = x^3 on the same set of axes
plt.plot(x_values, y_values, color='orange', label='$h(x) = x^3$')

# Add labels and title
plt.xlabel('Value of x')
plt.ylabel('Frequency / $h(x)$')
plt.title('Histogram of Normal Distribution and Plot of $h(x) = x^3$')

# Add legend
plt.legend()

# Show the plot
plt.show()