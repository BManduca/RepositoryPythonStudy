import pandas as pd

import matplotlib.pyplot as plt

iris = pd.read_csv(
        'iris.csv', 
        names=[
            'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'
        ]
    )

wine_reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)

# wine_reviews.head()

# fig, ax = plt.subplots();

# data = wine_reviews['country'].value_counts()

# style = data.index

# frequency = data.values

# ax.bar(style, frequency)

# ax.set_title('Wine Review Scores')
# ax.set_xlabel('Country')
# ax.set_ylabel('Frequency')


fig2, ax2 = plt.subplots()

data2 = iris['class'].value_counts()

style2 = data2.index

frequency2 = data2.values

ax2.bar(style2, frequency2)

ax2.set_title('Iris Species')
ax2.set_xlabel('Species')
ax2.set_ylabel('Frequency')
