"""
    vertically (row-wise)
    horizontally (column-wise)

    pd.concate([df1, df2], axis=0, ignore_index=True)

    [df1, df2] =
    axis = 1

    ignore_index = True/False
"""

# Vertical Concatenation
import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'CustomerName': ['Alice', 'Bob']
})

# DataFrame 2
df2 = pd.DataFrame({
    'CustomerID': [3, 4],
    'CustomerName': ['Charlie', 'David']
})

df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print("Vertical Concatenation:")
print(df_concat)

# Horizontal Concatenation
df_concat = pd.concat([df1, df2], axis=1, ignore_index=True)
print("\nHorizontal Concatenation:")
print(df_concat)