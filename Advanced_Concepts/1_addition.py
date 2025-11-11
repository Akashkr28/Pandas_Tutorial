# Adding Columns
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Jagdish', 'Raj'],
    "Age": [25, 30, 35, 40, 28, 33, 45, 29],
    "Salary": [40000, 60000, 70000, 20000, 55000, 65000, 90000, 58000],
    "Performance Score": [85, 90, 78, 88, 92, 80, 75, 89]
}

df = pd.DataFrame(data)
print(df)

# Square Brackets Method : df['New_Column'] = values
df['Bonus'] = df['Salary'] * 0.10
print(df)

# Using insert() Method : df.insert(loc, 'New_Column', values)
df.insert(0, "Employee ID", [101, 102, 103, 104, 105, 106, 107, 108])
print(df)