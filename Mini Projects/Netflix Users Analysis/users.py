import pandas as pandas
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
data=pandas.read_csv('data.csv')
df=pandas.DataFrame(data)
df['datatime']=pandas.to_datetime(df['datetime'],format='%Y-%m-%d %H:%M:%S',errors='coerce')
df['release_date']=pandas.to_datetime(df['release_date'],format='%Y-%m-%d',errors='coerce')
df['duration'] = pandas.to_numeric(df['duration'], errors='coerce') 

user_data = df.groupby('user_id').agg({
    'duration': ['sum', 'mean', 'count'],
    'genres': lambda x: len(set(','.join(x).split(',')))
}).reset_index()
print(user_data)
user_data.columns = ['user_id', 'total_watch_time', 'avg_watch_time', 'session_count', 'unique_genres']
print(user_data)

# Clustering
features = user_data[['total_watch_time', 'avg_watch_time', 'session_count', 'unique_genres']]
scaled = StandardScaler().fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
user_data['cluster'] = kmeans.fit_predict(scaled)

sns.pairplot(user_data, hue='cluster', diag_kind='kde', palette='tab10')
plt.suptitle("User Behavior Clusters", y=1.02)
plt.show()
