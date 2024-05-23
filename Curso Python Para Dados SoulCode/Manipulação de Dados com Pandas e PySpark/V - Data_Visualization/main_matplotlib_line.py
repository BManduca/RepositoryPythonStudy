import pandas as pd

import matplotlib.pyplot as plt

iris = pd.read_csv(
        'iris.csv', 
        names=[
            'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'
        ]
    )

wine_reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)

# eliminando a coluna que não tem valor númerico
columns = iris.columns.drop(['class'])

# shape é para dizer o tamanho do dataset
x_data = range(0, iris.shape[0])

fig, ax = plt.subplots()

for column in columns:
    ax.plot(x_data, iris[column], label=column)
    
ax.set_title('Iris Dataset')

ax.legend()

