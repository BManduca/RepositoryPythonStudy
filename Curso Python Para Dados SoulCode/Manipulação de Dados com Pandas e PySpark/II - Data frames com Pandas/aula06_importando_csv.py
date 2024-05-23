import numpy as np
import pandas as pd

df_csv = pd.read_csv('/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/Data frames com Pandas/Food_Preference.csv')

# print(df_csv)
# imprimindo as 3 primeiras linhas
# print(df_csv.head(3))

# imprimindo as 3 últimas linhas
print(df_csv.tail(3))