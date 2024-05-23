import pandas as pd

import seaborn as sbn

super_sales = pd.read_csv(
    'supermarket_sales.csv', names=[
        'Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating'
    ]
)

"""
Invoice ID,Branch,City,Customer type,Gender,Product line,Unit price,Quantity,Tax 5%,Total,Date,Time,Payment,cogs,gross margin percentage,gross income,Rating
"""


# super_sales = pd.read_csv('supermarket_sales.csv', index_col=0)

# super_sales.head()

# sbn.scatterplot(x='Branch', y='Gender', data=super_sales)

sbn.displot(super_sales['Rating'], bins=10, kde=True)

# sbn.countplot(super_sales['Payment'])
