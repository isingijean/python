import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "Score": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)

# Filtering students with Score > 85
filtered_df = df[df["Score"] > 85]
print("Students with score > 85:\n", filtered_df)
