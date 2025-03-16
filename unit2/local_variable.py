# Function to calculate the area of a rectangle
def compute_area(length, width):
    area = length * width  # Formula for area of a rectangle
    return area

# Input: Length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Compute the area
area = compute_area(length, width)

# Output: Display the area
print(f"The area of the rectangle is: {area} square units")
