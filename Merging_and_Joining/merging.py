# Method: pd,merge(df1,df2,on='Column Name', how='type of join')
import pandas as pd

# Customer DataFrame

df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

# Orders DataFrame
df_orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 3, 5],
    'OrderAmount': [250, 150, 300, 400] 
})

# Merge
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')
print("Inner Join:")
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='outer')
print("\nOuter Join:")
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='left')
print("\nLeft Join:")
print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='right')
print("\nRight Join:")
print(df_merged)