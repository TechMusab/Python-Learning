# DRAGON REAL ESTATE PROJECT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump, load

# Load dataset
housing = pd.read_csv("data.csv")

# Initial data checks
housing.head()
housing.info()
housing['CHAS'].value_counts()
housing.describe()

# Plot histograms
housing.hist(bins=50, figsize=(20, 15))


# def spilt_test_train(data, testratio):
# np.random.seed(42)
# shuffled = np.random.permutation(len(data))
# test_set_size = int(len(data) * testratio)
# test_indices = shuffled[:test_set_size]
# train_indices = shuffled[test_set_size:]
# return data.iloc[test_indices], data.iloc[train_indices]

# test_set, train_set = spilt_test_train(housing, 0.2)
# print("Rows in test set:", len(test_set))
# print("Rows in train set:", len(train_set))


# Random split using sklearn
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print("Rows in test set:", len(test_set))
print("Rows in train set:", len(train_set))

# Stratified split using CHAS feature
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['CHAS']):
    start_train_set = housing.loc[train_index]
    start_test_set = housing.loc[test_index]

# Check CHAS distribution
start_train_set['CHAS'].value_counts()
start_test_set['CHAS'].value_counts()

# Prepare training data
housing = start_train_set.copy()
housing = start_train_set.drop('MEDV', axis=1)
housing_labels = start_train_set['MEDV'].copy()

# Scatter matrix and correlation plots
# attr = ['MEDV', 'RM', 'ZN', 'LSTAT']
# scatter_matrix(housing[attr], figsize=(20, 15))
# housing.plot(kind='scatter', x='RM', y='MEDV', alpha=0.7)
# housing['TAXRM'] = housing['TAX'] / housing['RM']
# housing.head()
# housing.dropna(subset=['RM']).shape


# Imputation
impute = SimpleImputer(strategy='median')
impute.fit(housing)
impute.statistics_
X = impute.transform(housing)
housing_tr = pd.DataFrame(X, columns=housing.columns)
housing_tr.describe()

# Preprocessing pipeline
mypipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('stdscaler', StandardScaler())
])
housing_num_tr = mypipeline.fit_transform(housing)
housing_num_tr.shape

# Model selection
# model = LinearRegression()
# model = DecisionTreeRegressor()
model = RandomForestRegressor()
model.fit(housing_num_tr, housing_labels)

# Predict using sample data
some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[0:5]
prepared_data = mypipeline.transform(some_data)
model.predict(prepared_data)
list(some_labels)

# Evaluate model using RMSE
housing_predications = model.predict(housing_num_tr)
mse = mean_squared_error(housing_labels, housing_predications)
rmse = np.sqrt(mse)
mse

# Cross-validation
scores = cross_val_score(model, housing_num_tr, housing_labels, scoring='neg_mean_squared_error', cv=10)
rmse_scores = np.sqrt(-scores)

# Print scores
def print_scores(scores):
    print("Score:", scores)
    print("Mean:", scores.mean())
    print("Standard Deviation:", scores.std())

print_scores(rmse_scores)

# Save model
dump(model, 'Dragon.joblib')

# Test the model
X_test = start_test_set.drop('MEDV', axis=1)
Y_test = start_test_set['MEDV'].copy()
X_test_prepared = mypipeline.transform(X_test)
final_predications = model.predict(X_test_prepared)
final_mse = mean_squared_error(Y_test, final_predications)
final_mse = np.sqrt(final_mse)

# Final results
print(final_predications, list(Y_test))
