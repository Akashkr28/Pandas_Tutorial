# Method: df["Column Name"].mean(), df["Column Name"].sum(), df["Column Name"].max(), df["Column Name"].min(), df["Column Name"].count()
import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [25, 22, 35],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()
print(f"Average Salary: {avg_salary}")