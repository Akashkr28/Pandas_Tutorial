# fillna() method to fill missing values with a specified value: df.fillna(value, inplace=True)
import pandas as pd

data = {
    'Name': ['Alice', None, 'Charlie', 'David', 'Eva', 'Frank', 'Jagdish', 'Raj'],
    "Age": [25, None, 35, 40, 28, 33, 45, 29],
    "Salary": [40000, None, 70000, 20000, 55000, 65000, 90000, 58000],
    "Performance Score": [85, None, 78, 88, 92, 80, 75, 89]
}

df = pd.DataFrame(data)
print(df)

# df.fillna(0, inplace=True)
# print("\nDataFrame after filling missing values with 0:")


df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nDataFrame after filling missing Age values with the mean age:")
print(df)