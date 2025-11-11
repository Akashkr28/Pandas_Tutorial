# Sample Data Frame
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Jagdish', 'Raj'],
    "Age": [25, 30, 35, 40, 28, 33, 45, 29],
    "Salary": [50000, 60000, 70000, 80000, 55000, 65000, 90000, 58000],
    "Preference Score": [85, 90, 78, 88, 92, 80, 75, 89]
}

df = pd.DataFrame(data)
print("Sample Data Frame")
print(df)
print("\nDescriptive Statistics")
print(df.describe())