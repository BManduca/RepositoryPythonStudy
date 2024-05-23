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

ax.scatter(iris['sepal_length'], iris['sepal_width'])

ax.set_title('Iris Dataset')

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
