# Non-empty containers evaluate to True
print(bool([1, 2, 3]))  # Output: True
print(bool({"key": "value"}))  # Output: True

# Empty containers evaluate to False
print(bool([]))  # Output: False
print(bool(()))  # Output: False
