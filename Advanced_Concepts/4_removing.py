# Updating Columns
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Jagdish', 'Raj'],
    "Age": [25, 30, 35, 40, 28, 33, 45, 29],
    "Salary": [40000, 60000, 70000, 20000, 55000, 65000, 90000, 58000],
    "Performance Score": [85, 90, 78, 88, 92, 80, 75, 89]
}

df = pd.DataFrame(data)
print(df)

# df.drop() Method : df.drop(columns=['Column1', 'Column2'], inplace=True)
print("\nRemoving 'Performance Score' column:")
df.drop(columns=['Performance Score'], inplace=True)
print(df)