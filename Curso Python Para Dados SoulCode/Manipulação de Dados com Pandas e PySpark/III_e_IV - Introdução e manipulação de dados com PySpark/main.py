import findspark
findspark.init()

# https://code.visualstudio.com/docs/python/jupyter-support-py

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *

spark = SparkSession.builder \
    .master("local") \
    .appName("Aula Introdutória PySpark") \
    .config("spark.executor.memory", "1gb") \
    .getOrCreate()
    
sc = spark.sparkContext

# puxamos o arquivo para dentro do rdd em questão 
rdd = sc.textFile('/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/III - Introdução a manipulação de dados com PySpark/salary_data2.csv')

# mapeamos e separamos por vírgula
rdd = rdd.map(lambda line: line.split(","))

# rdd.take(5)

# rdd.first()

# rdd_new.take(7)

"""
    => agora não é mais um rdd e sim um Dataframe
    
    => o row faz com a gente atríbua os nossos textos para as informações que 
    estão sendo tratadas no DF por exemplo
    e a posição são verificadas através índices.
    
    => toDF() converte de rdd para um dataframe
"""
df = rdd.map(lambda line: Row(AnosExperiencia=line[0], Salario=line[1])).toDF()

# df.show()

df.printSchema()


# dataframe que será analisado, nomes são os nomes das colunas e o novoTipo
# será o novo tipo de dado designado para as informações
def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe

colunas = ['AnosExperiencia', 'Salario']

new_df = converterColuna(df, colunas, FloatType())

# new_df.select('Salario').show(10)

# new_df.groupby('Salario').count().sort('Salario', ascending=False).show()

# new_df.describe().show()

# new_df.collect()

# new_df.filter(new_df['Salario'] > 5000).show()

# new_df.select('Salario').filter(new_df['Salario'] > 5000).show()

# new_df.filter((df['Salario'] > 5000) & (df['AnosExperiencia'] > 2)).show()

new_df.filter((df['Salario'] > 5000) | (df['AnosExperiencia'] > 2)).show()
