#head & tail
import pandas as pandas
df=pandas.read_csv("sales_data.csv",encoding="latin1")
print(df.head(5))
print(df.tail(5))
print(df.info())
company_data={
    "name":["Abdullah","Ali","Aisha","Sara","Ahmed"],
    "age":[28,34,29,25,30],
    "city":["New York","Los Angeles","Chicago","Houston","Phoenix"],
    "salary":[70000,80000,60000,75000,90000],
    "department":["HR","IT","Finance","Marketing","Sales"]
}
df2=pandas.DataFrame(company_data)
print(df.describe())
print(df2.describe())
print("Shape:",df2.shape)
print("Columns Names:",df2.columns)