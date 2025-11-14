# Sorting Data

# Sorting Data in 1 Column: sort_values()
# df.sort_values(by="Column Name", ascending=True, descending=False, inplace=True)

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [25, 22, 35],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df.sort_values(by="Age", ascending=False, inplace=True)
print("\nDataFrame sorted by Age in descending order:")
print(df)