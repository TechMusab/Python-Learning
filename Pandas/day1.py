import pandas as pandas
#Load Dataset
df=pandas.read_csv("sales_data.csv",encoding="latin1")
jsondata=pandas.read_json("sales_data.json",encoding="latin1")
print(df)
print(jsondata)
#save data
data={
    "name":["John","Doe","Jane"],
    "age":[28,34,29],
    "city":["New York","Los Angeles","Chicago"],
    "salary":[70000,80000,60000],
}
df2=pandas.DataFrame(data)
print(df2)
df2.to_csv("output.csv",index=False)
df2.to_excel("output.xlsx",index=False)
df2.to_json("output.json",index=False)
# Selecting single column
print(df2["age"])
# Selecting multiple columns
print(df2[["name","age"]])
#Filtering rows
high_salary = df2[df2["salary"]> 70000]
print(high_salary)
#Filtering with multiple conditions
high_salary_and_age = df2[(df2["salary"] > 70000) & (df2["age"] < 30)]
print(high_salary_and_age)
#using OR
high_salary_or_age = df2[(df2["salary"] > 70000) | (df2["age"] < 30)]
print(high_salary_or_age)