import numpy as np
import pandas as pd

df_csv = pd.read_csv('/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/Data frames com Pandas/Food_Preference.csv')

# print(df_csv['Food'].unique())

# quantidade de registros/dados presente na coluna Nationality
# print(df_csv['Nationality'].value_counts())

# print(df_csv)
# agrupando por um parametro especifico e mostrando a media das colunas existentes para cada registro mostrado de acordo com param escolhido
# print(df_csv.groupby('Age').mean())

# ---------------------------------------------------------------

# criando outro dataframe novo com as primeiras cinco posicoes do df_csv
df2 = df_csv.head()
# print(df2)

df3 = df2.replace({"Dessert":{'Yes':'No'}})
# print(df3)

df4 = df3.replace({"Age":{31:np.nan}})
# print(df4)

# dropna é uma função para remover valores resultados de um erro ou NaN
df5 = df4.dropna()

print(df5)
