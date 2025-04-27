import pandas as pandas
data={
    'Name': ['John',None, 'Anna', 'Peter', 'Linda'],
    'Age': [28,None, 24, 35, 32],
    'salary':[50000,None, 60000, 70000, 80000]
}
df=pandas.DataFrame(data)
print(df)
# df["Bonus"]=df["salary"] * 0.1
# print(df)
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
