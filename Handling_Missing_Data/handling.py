# dropna() Method : df.dropna(axis = 0, inplace=True) to remove rows with any missing values
import pandas as pd

data = {
    'Name': ['Alice', None, 'Charlie', 'David', 'Eva', 'Frank', 'Jagdish', 'Raj'],
    "Age": [25, None, 35, 40, 28, 33, 45, 29],
    "Salary": [40000, None, 70000, 20000, 55000, 65000, 90000, 58000],
    "Performance Score": [85, None, 78, 88, 92, 80, 75, 89]
}

df = pd.DataFrame(data)
print(df)

# Removing rows with any missing values
df.dropna(inplace=True)
print("\nDataFrame after removing rows with missing values:")
print(df)