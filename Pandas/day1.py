import pandas as pandas
#Load Dataset
# df=pandas.read_csv("sales_data.csv",encoding="latin1")
# jsondata=pandas.read_json("sales_data.json",encoding="latin1")
# print(df)
# print(jsondata)
#save data
data={
    "name":["John","Doe","Jane"],
    "age":[28,34,29],
    "city":["New York","Los Angeles","Chicago"]
}
df=pandas.DataFrame(data)
print(df)
df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)
