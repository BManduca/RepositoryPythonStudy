from pyspark.sql.session import SparkSession


from pyspark.sql.types import (BooleanType, IntegerType, StringType, TimestampType, StructType, StructField, ArrayType, 
FloatType, DateType)


import pyspark.sql.functions as F


spark = SparkSession.builder.appName('firstSession')\
    .config('spark.master', 'local[4]')\
    .config('spark.executor.memory', '1gb')\
    .config('spark.shuffle.partitions', 1)\
    .getOrCreate()
    
schema = StructType([
    StructField('case_id', IntegerType()),
    StructField('date', DateType()),
    StructField('county', StringType()),
    StructField('state', StringType()),
    StructField('cases', IntegerType()),
    StructField('deaths', IntegerType())
])

path = "/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/III - Introdução a manipulação de dados com PySpark/us-counties-recent.csv"

df = spark.read.format('csv')\
    .schema(schema)\
    .load(path)
        
# df.printSchema()


# df.filter(df['state'] == 'Arkansas').show()

# cases = df.withColumnRenamed('case_id', 'caseId')

# cases = df.toDF(*['ID', 'Data', 'Condado', 'Estado', 'Casos', 'Mortes'])

# cases.show()

# df2 = df.select('county', 'state', 'cases')
# df2.show()


df3 = df.sort(F.desc('cases'))

df3.show()