# Global variable x initialized with a value of 10
x = 10
# Global variable y initialized with a value of 20
y = 20
# Function to calculate the sum of the global variables x and y
def sum():
    # Accessing global variables x and y
    sum = x + y
    return sum

# Print the result of the sum function
# sum() => Function call
print(f"Sum of {x} and {y} is = {sum()}")
