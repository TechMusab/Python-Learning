import pandas as pandas
data={
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'salary':[50000, 60000, 70000, 80000]
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
