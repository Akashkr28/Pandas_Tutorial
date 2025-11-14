import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [25, 22, 35],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Method: df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)

df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print("\nDataFrame sorted by Age (asc) and Salary (desc):")
print(df)