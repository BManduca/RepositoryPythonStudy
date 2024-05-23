"""
libraries = [
    pip3 install plotly==5.20.0
    pip3 install nbformat
]
"""


import plotly.express as px

# Dataset Geral
df = px.data.gapminder().query("country=='Canada'")

#gráfico de linha
# fig = px.line(df, x="year", y="lifeExp", title="Life Expectancy in Canada")
# fig.show()


# gráfico estilo histograma
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill")
# fig.show()

# gráfico de scatter
fig = px.scatter(x=[0,1,2,3,4,5,6,7,8,9,10], y=[0,2,4,6,8,10,12,14,16,18,20])
fig.show()

