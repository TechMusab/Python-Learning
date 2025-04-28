import pandas as pandas
students={
    'Name':['John','Anna','Peter','Linda'],
    'Age':[23,22,22,23],
    'Marks':[85, 90, 78, 88],
    
}
cities={
    'city':['New York','Los Angeles','Chicago','Houston'],
}
df=pandas.DataFrame(students)
df2=pandas.DataFrame(cities)
#print student marks greater than 80
name=df[df['Marks'] > 80]
print(name)
#Calculate average marks by Age group.
avrgmarks=df.groupby('Age')['Marks'].mean()
print(avrgmarks)
#Add a new column "Grade" based on Marks.
df['Grade']=df['Marks'].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else 'C'))
print(df)
# Merge two DataFrames: Students and their City.
df3=pandas.merge(df,df2,left_index=True,right_index=True)
print(df3)