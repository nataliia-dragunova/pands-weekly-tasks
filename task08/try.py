import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 values from a normal distribution with mean 5 and standard deviation 2
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Plot the histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution (Mean = 5, Std Dev = 2)')

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 values from a normal distribution with mean 5 and standard deviation 2
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Plot the histogram of the normal distribution
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution')

# Define the function h(x) = x^3
def h(x):
    return x**3

# Generate x values from 0 to 10
x_values = np.linspace(0, 10, 100)
# Evaluate h(x) for each x
y_values = h(x_values)

# Plot the function h(x) = x^3
plt.plot(x_values, y_values, color='red', label='$h(x) = x^3$')

# Set labels and legend
plt.xlabel('x')
plt.ylabel('Frequency / $h(x)$')
plt.legend()

# Show the plot
plt.show()
