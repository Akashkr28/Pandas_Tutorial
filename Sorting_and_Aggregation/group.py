import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun', 'Narun', 'Tarun'],
    "Age": [25, 22, 35, 22, 25],
    "Salary": [50000, 60000, 45000, 52000, 480000]
}

df = pd.DataFrame(data)

grouped= df.groupby("Age")["Salary"].sum()
print(grouped)