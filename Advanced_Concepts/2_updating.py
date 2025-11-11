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

# .loc[] Method : df.loc[row_index, 'Column_Name'] = new_value
df.loc[0, 'Salary'] = 45000  # Update Alice's Salary
print(df)