#head & tail
import pandas as pandas
df=pandas.read_csv("sales_data.csv",encoding="latin1")
print(df.head(5))
print(df.tail(5))
