import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
scores = pd.read_csv('student_scores.csv')
df= pd.DataFrame(scores)
# Cleaning Data
df.fillna(0, inplace=True)
# Average Scores per subject
avgmath=df['Math'].mean()
avgenglish=df['English'].mean()
avgscience=df['Science'].mean()
print(avgmath)
print(avgenglish)
print(avgscience)

# Assigning grades using Numpy select
conditionsmath = [
    (df['Math'] >= 90),
    (df['Math'] >= 80) & (df['Math'] < 90),
    (df['Math'] >= 70) & (df['Math'] < 80),
    (df['Math'] >= 60) & (df['Math'] < 70),
    (df['Math'] >= 50) & (df['Math'] < 60),
    (df['Math'] < 50)
]
conditionsenglish = [
    (df['English'] >= 90),
    (df['English'] >= 80) & (df['English'] < 90),
    (df['English'] >= 70) & (df['English'] < 80),
    (df['English'] >= 60) & (df['English'] < 70),
    (df['English'] >= 50) & (df['English'] < 60),
    (df['English'] < 50)
]
conditionsscience = [
    (df['Science'] >= 90),
    (df['Science'] >= 80) & (df['Science'] < 90),
    (df['Science'] >= 70) & (df['Science'] < 80),
    (df['Science'] >= 60) & (df['Science'] < 70),
    (df['Science'] >= 50) & (df['Science'] < 60),
    (df['Science'] < 50)
]
grades=['A','B','C','D','E','F']
df['Math Grade'] = np.select(conditionsmath, grades,default='F')
df['English Grade'] = np.select(conditionsenglish, grades,default='F')
df['Science Grade'] = np.select(conditionsscience, grades,default='F')
# Adding total score column
df['Total']=df[['Math','English','Science']].sum(axis=1)
# Filtering Passed Students
passed=df[df['Total']>=150]
print(passed)
df.to_csv("student_result_analysis.csv", index=False)
# Graphs
plt.figure(figsize=(8, 5))
sns.countplot(x="Math Grade", data=df, order=sorted(df["Math Grade"].unique()))
plt.title("Math Grade")
plt.xlabel("Math Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
#plt.show()

subject_means = df[["Math", "English", "Science"]].mean()
plt.figure(figsize=(8, 5))
sns.barplot(x=subject_means.index, y=subject_means.values)
plt.title("Average Marks per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()
