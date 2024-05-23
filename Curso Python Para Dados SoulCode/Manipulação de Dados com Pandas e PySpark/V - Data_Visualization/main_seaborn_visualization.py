import pandas as pd

import seaborn as sbn

iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
# wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', names=['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety', 'winery'])

# wine_reviews.head()

sbn.scatterplot(x='sepal_length', y='sepal_width', data=iris)

# sbn.displot(wine_reviews['points'], bins=10, kde=True)

# sbn.countplot(wine_reviews['points'])