## Hadoop
    
- " É um framework para desenvolvimento de aplicações distribuídas ", 
"com alta escalabilidade, confiabilidade e tolerância a falhas, subdividido em três projetos: Hadoop Commons, Hadoop Distribuited File System e Hadoop MapReduce."
    
### ARMAZENAMENTO DE DADOS
- O Hadoop Distribuited File System (HDFS) fornece armazenamento escalável e tolerante a falhas, o custo-eficiente para o seu lago de dados grande.

- Projetado para abranger grandes clusters de servidores.

- Será trabalhado com datasets com gigas de dados como jsons ou csvs
        
### PROCESSAMENTO DE DADOS
- MapReduce é o quadro original para escrever aplicações massivamente 
paralelas que processam grandes quantidades de dados estruturados e não estruturados armazenados no HDFS.
        
### ACESSO E ANÁLISE DE DADOS
- Os aplicativos podem interagir com os dados no Hadoop usando lote ou SQL
interativa (Apache Hive) ou o acesso de baixa latência com NoSQL (HBase)
        
        
### VANTAGENS
- Capacidade de armazenar e processar grandes quantidades de qualquer tipo 
de dado, e rapidamente.
- Poder computacional
- Tolerância a falhas
- Flexibilidade
- Custo baixo
- Escalabilidade
        
### Apache Spark
- É uma ferramenta Big Data que tem o objetivo de processar grandes conjuntos de dados de forma paralela e distribuída.
        
### Apache Spark Core (soma dos 4 itens abaixo resulta no Core do Apache Spark)
- Spark SQL
- Spark Streaming
- MLlib (machine learning)
- GraphX (graph)
        
        
- Spark Streaming, que possibilita o processamento de fluxos em tempo real
- O GraphX, que realiza o processmento sobre grafos
- o SparkSQL para a utilização de SQL na realização de consultas e processamentos sobre os dados no Spark
- A MLlib, que é a biblioteca de aprendizado de máquina, com diferentes algoritmos para as mais diversas atividades, como clustering.
    
### Principais componentes
- Resilient Distributed Datasets (RDD)
- Operações
- Spark Context
        
### PySpark 
- É uma biblioteca spark escrita em Python para executar o aplicativo Python usando recursos Apache Spark. Usando o PySpark podemos executar aplicativos paralelamente no cluster distribuído (vários nós)


### Vantagens
- PySpark é um mecanismo de processamento distribuído de propósitio gerak, na memória, que permite processar dados de forma eficiente e de forma distribuída.
- As aplicações em execução no PySpark são 100x mais rápidas que os sistemas tradicionais.
- Você terá grandes benefícios usando o PySpark para ingestão de dados
- Usando o PySpark, podemos processar dados de Hadoop HDFS, AWS S3 e muitos sistemas de arquivos.
- Usando o streaming PySpark, você também pode transmitir arquivos do sistema de arquivos e também transmitir a partir do soquete.
- PySpark tem bibliotecas de aprendizado de máquina e gráficos.


## Gerenciadores
- Autônomo
- Apache Mesos
- Hadoop YARN
- Kubernetes


## Install Spa
sudo apt update -y
sudo apt install default-jdk -y
wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz

tar -xvzf spark-*

sudo mv spark-3.5.1-bin-haddop3/ /opt/spark/

echo "export SPARK_HOME=/opt/spark" >> ~/.profile
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile

source ~/.profile

start-master.sh


## Comandos
- criando um rdd
    >
        rdd = sc.textFile('/home/ahgora/Manduca/MyGitHub/PythonStudy/Curso Python Para Dados SoulCode/Manipulação de Dados com Pandas e PySpark/III - Introdução a manipulação de dados com PySpark/salary_data2.csv')

- pegando as 5 primeiras posições do rdd (resilient distributed dataset)
    >
        rdd.take(5)

- pegando a primeira linha do rdd
    >
        rdd.first()

- transformando um rdd em um DF
    > 
        df = rdd.map(lambda line: Row(AnosExperiencia=line[0], Salario=line[1])).toDF()

- imprimindo o DF
    >
        df.show()

- realizando consulta no DF, através de uma coluna especifica e mostrando uma quantidade X
    > 
        new_df.select('Salario').show(10)

- realizando um groupby em uma coluna e também retornando um count da quantidade dos salarios existentes, trazendo os dados de maneira descendente
    > 
        new_df.groupby('Salario').count().sort('Salario', ascending=False).show()

- recolhendo informações estatisticas do DF
    > 
        new_df.describe().show()

- imprimindo o DF como se fosse uma matriz
    >
        new_df.collect()

- Realizando consultas através de condicionais
    - filtrando salarios maiores que 5000
        >
            new_df.filter(new_df['Salario'] > 5000).show()

    - filtrando salarios maiores que 5000 e anos de experiencia maiores que 2
        >
            new_df.filter((df['Salario'] > 5000) & (df['AnosExperiencia'] > 2)).show()


    - filtrando salarios maiores que 5000 ou anos de experiencia maiores que 2
        >
            new_df.filter((df['Salario'] > 5000) | (df['AnosExperiencia'] > 2)).show()

- Para criar o schema de um csv em especifico
    > 

        from pyspark.sql.session import SparkSession


        from pyspark.sql.types import (BooleanType, IntegerType, StringType, 
                TimestampType, StructType, 
                StructField, ArrayType, 
                FloatType, DateType)

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

        df.printSchema()


- Modificando o nome de uma única coluna
    >
        cases = df.withColumnRenamed('case_id', 'caseId')

- Modificando o nome de todas as colunas
    >
        cases = df.toDF(*['ID', 'Data', 'Condado', 'Estado', 'Casos', 'Mortes'])
    

- Criando um novo DF através do nosso DF base, contendo somente algumas colunas
    >
        df2 = df.select('county', 'state', 'cases')
        df2.show()