import pandas as pd

import matplotlib.pyplot as plt

iris = pd.read_csv(
        'iris.csv', 
        names=[
            'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'
        ]
    )

wine_reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)

fig, ax = plt.subplots()

ax.hist(iris['class'])

ax.set_title('Iris Species')
ax.set_xlabel('Species')
ax.set_ylabel('Frequency')
