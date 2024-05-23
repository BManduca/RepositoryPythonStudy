from pyspark.sql.session import SparkSession


"""
   age,workclass,fnlwgt,education,educational-num,marital-status,occupation,relationship,race,gender,capital-gain,capital-loss,hours-per-week,native-country,income
"""

from pyspark.sql.types import (DoubleType, IntegerType, 
                               StringType, TimestampType, 
                               StructType, StructField, ArrayType, 
                               FloatType, DateType, BooleanType)


import pyspark.sql.functions as F


spark = SparkSession.builder.appName('firstSession')\
    .config('spark.master', 'local[4]')\
    .config('spark.executor.memory', '1gb')\
    .config('spark.shuffle.partitions', 1)\
    .getOrCreate()
    
schema = StructType([
    StructField('Age', IntegerType()),
    StructField('Workclass', StringType()),
    StructField('Fnlwgt', IntegerType()),
    StructField('Education', StringType()),
    StructField('Educational-Num', IntegerType()),
    StructField('Marital-Status', StringType()),
    StructField('Occupation', StringType()),
    StructField('Relationship', StringType()),
    StructField('Race', StringType()),
    StructField('Gender', StringType()),
    StructField('Capital-gain', IntegerType()),
    StructField('Capital-loss', IntegerType()),
    StructField('Hours-per-week', IntegerType()),
    StructField('Native-country', StringType()),
    StructField('Income', StringType())
])

path = '/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/III - Introdução a manipulação de dados com PySpark/exerc_final/adult.csv'

df = spark.read.format('csv')\
    .schema(schema)\
    .load(path)

def converterColuna(dataframe, nomes, newType):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(newType))
    return dataframe

columns = ['Age']

new_df = converterColuna(df, columns, FloatType())

"""
1.    Imprima o Schema de seu DF;
2.    Imprima os primeiros 5 linhas de seu DF;
3.    Converta o campo idade do tipo inteiro para o tipo Float (ou vice versa, dependendo do seu Schema);
4.    Exiba somente 5 itens com os campos "age" e "education";
5.    Agrupe a quantidade de itens em "education" ordenados de maneira ascendente;
6.    Exiba um describe da tabela "capital_gain";
"""

    
# df.printSchema()

# df.take(5)

# df.show(5)

# new_df.printSchema()

# new_df.show()

# new_df.select('Age', 'Education').show(5)

# new_df.groupby('Education').count().sort('Education', ascending=True).show()

new_df.describe(['Capital-gain']).show()
