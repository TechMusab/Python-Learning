import pandas as pandas
data={
    'Name': ['John',None, 'Anna', 'Peter', 'Linda'],
    'Age': [28,None, 24, 35, 32],
    'salary':[50000,None, 60000, 70000, 80000]
}
df=pandas.DataFrame(data)
print(df)
#using insert method
df.insert(2, "Bonus", df["salary"] * 0.1)
print(df)
#updating data
df.loc[1, "Bonus"] = 10000
print(df)
#Updating Salary
df["salary"]=df["salary"]*1.1
print(df)
#Removing column
df.drop(columns=["Bonus","Age"],inplace=True)
print(df)
# Checking Missing data
print(df.isnull().sum())
# Handling Missing Data
# df.dropna(axis=0,inplace=True)
# print(df)
# df["salary"].fillna(df["salary"].mean(), inplace=True)
# print(df)

df['salary']=df["salary"].interpolate(method="linear")
print(df)
#Sorting Values
df.sort_values(by="salary", ascending=False, inplace=True)
print(df)
# Sorting values based on multiple columns
df.sort_values(by=["salary","Name"], ascending=[True,False], inplace=True)
print(df)
# Aggregation
print(df['salary'].sum())
print(df['salary'].mean())
print(df['salary'].max())
print(df['salary'].min())
#Grouping
newdata={
    'Name': ['John',None, 'Anna', 'Peter', 'Linda'],
    'Age': [28,None, 28, 32, 32],
    'salary':[50000,None, 60000, 70000, 80000]
}
df2=pandas.DataFrame(newdata)
print(df2.groupby("Age")["salary"].sum())
# Merging & Joining
customers_data={
    'CustomerID': [1, 2, 3,5,6,7,8,9,10],
    'CustomerName': ['Alfred', 'Maria', 'John', 'Linda','Sara','Tom','Jerry','Anna','Mike'],
    'Country': ['USA', 'USA', 'UK', 'Canada','USA','UK','Canada','USA','UK']
}
order_data={
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 3, 4,5],
    'OrderAmount': [250.50, 150.75, 300.00, 400.25, 500.00],
}
dfcustomers=pandas.DataFrame(customers_data)
dforders=pandas.DataFrame(order_data)
innermerged=pandas.merge(dfcustomers,dforders, on='CustomerID', how='inner')
print(innermerged)
outermerged=pandas.merge(dfcustomers,dforders, on='CustomerID', how='outer')
print(outermerged)
leftmerged=pandas.merge(dfcustomers,dforders, on='CustomerID', how='left')
print(leftmerged)
rightmerged=pandas.merge(dfcustomers,dforders, on='CustomerID', how='right')
print(rightmerged)


