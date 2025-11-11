import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Jagdish', 'Raj'],
    "Age": [25, 30, 35, 40, 28, 33, 45, 29],
    "Salary": [40000, 60000, 70000, 20000, 55000, 65000, 90000, 58000],
    "Performance Score": [85, 90, 78, 88, 92, 80, 75, 89]
}

df = pd.DataFrame(data)

# Filtering rows where salary > 50000, single condition
high_salary = df[df['Salary'] > 50000]
print("Employees with Salary greater than 50000:")
print(high_salary)

# Filtering rows where salary  > 50000 and age > 30000, multiple conditions
filtered  = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print("\nEmployees with Salary greater than 50000 and Age greater than 30:")
print(filtered)

# Filtering rows using OR condition
or_filtered = df[(df['Age'] > 35) | (df['Performance Score'] > 90)]
print("\nEmployees with Age greater than 35 or Performance Score greater than 90:")
print(or_filtered)