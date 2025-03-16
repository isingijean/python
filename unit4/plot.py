import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# Creating a line plot
plt.plot(x, y, marker='o', linestyle='--', color='b', label="Growth")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Simple Line Plot")
plt.legend()
plt.show()
