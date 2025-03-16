# Original string
original = "Hello World!"
# Remove "World"
substring_to_remove = "World"
new_string = original.replace(substring_to_remove, "")
# Strip extra spaces if necessary
new_string = new_string.strip()
print(new_string)
