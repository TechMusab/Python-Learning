import pandas as pandas
data=pandas.read_csv('data.csv')
df=pandas.DataFrame(data)
df['datatime']=pandas.to_datetime(df['datetime'],format='%Y-%m-%d %H:%M:%S',errors='coerce')
df['release_date']=pandas.to_datetime(df['release_date'],format='%Y-%m-%d',errors='coerce')
df['duration'] = pandas.to_numeric(df['duration'], errors='coerce') # errors ='coerce' will convert non-numeric values to NaN

#Feature Engineering
user_data = df.groupby('user_id').agg({
    'duration': ['sum', 'mean', 'count'],
    'genres': lambda x: len(set(','.join(x).split(',')))
}).reset_index()
print(user_data)
user_data.columns = ['user_id', 'total_watch_time', 'avg_watch_time', 'session_count', 'unique_genres']
print(user_data)