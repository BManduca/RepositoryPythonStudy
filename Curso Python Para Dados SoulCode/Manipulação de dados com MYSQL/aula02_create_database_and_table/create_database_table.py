import pymysql

colors = ('\033[0m',  # 0 - SEM CORES
          '\033[0;31m',  # 1 - VERMELHO
          '\033[0;32m',  # 2 - VERDE
          '\033[0;33m',  # 3 - AMARELO
          '\033[0;34m',  # 4 - AZUL
          '\033[0;35m',  # 5 - ROXO
          '\033[0;30m'  # 6 - BRANCO
          )


def imprimirMensagem(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^60}')
    print(colors[0], end='')


def imprimirLinha(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')


# realizando uma conexao remota
# db = pymysql.connect(
#     host='212.1.211.51', => para se conectar com uma base remota
#     user='Manduca', => o usuário
#     password='h3H@rSAuDK)@!Eu_', => senha
#     db = 'nome_library_database' => nome do banco para fazer a conexao
# )

db = pymysql.connect(
    host='localhost',
    user='Manduca',
    password='h3H@rSAuDK)@!Eu_',
    database='mydatabase'
)

# variável de instanciamento do nosso banco de dados
cursor = db.cursor()
# cursor.execute('CREATE DATABASE mydatabase')
# imprimirLinha(4)
# imprimirMensagem('DATABASE CRIADA COM SUCESSO!', 2)
# imprimirLinha(4)

# cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# imprimirLinha(4)
# imprimirMensagem('TABELA CRIADA COM SUCESSO!', 2)
# imprimirLinha(4)

cursor.execute(
    "SELECT * FROM `customers`"
)

numrows = int(cursor.rowcount)
result = cursor.fetchall()
imprimirLinha(4)
print()
imprimirMensagem(f'Número total de registros encontrados: {numrows}', 4)
print()
imprimirLinha(4)
for i in result:
    print(i)
imprimirLinha(4)
print()

