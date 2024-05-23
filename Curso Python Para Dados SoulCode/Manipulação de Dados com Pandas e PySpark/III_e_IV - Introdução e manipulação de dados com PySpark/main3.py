from pyspark.sql.session import SparkSession


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
    StructField('RecordNumber', IntegerType()),
    StructField('Zipcode', IntegerType()),
    StructField('ZipCodeType', StringType()),
    StructField('City', StringType()),
    StructField('State', StringType()),
    StructField('LocationType', StringType()),
    StructField('Lat', DoubleType()),
    StructField('Long', DoubleType()),
    StructField('Xaxis', DoubleType()),
    StructField('Yaxis', DoubleType()),
    StructField('Zaxis', DoubleType()),
    StructField('WorldRegion', StringType()),
    StructField('Country', StringType()),
    StructField('LocationText', StringType()),
    StructField('Location', StringType()),
    StructField('Decommisioned', BooleanType()),
    StructField('TaxReturnsFiled', IntegerType()),
    StructField('EstimatedPopulation', IntegerType()),
    StructField('TotalWages', IntegerType()),
    StructField('Notes', StringType())
])

path = "/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/III - Introdução a manipulação de dados com PySpark/zipcodes.json"

df = spark.read.schema(schema)\
    .json(path)
            
# df.printSchema()
# df.show()


df.registerTempTable('zipcodes')

# output = spark.sql('SELECT * FROM zipcodes')

output = spark.sql('SELECT RecordNumber, Zipcode, City FROM zipcodes WHERE RecordNumber > 10')

output.show()
