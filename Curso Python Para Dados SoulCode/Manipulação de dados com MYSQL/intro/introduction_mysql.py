import pymysql

# db = pymysql.connect(host="localhost",
#                      user="Manduca",
#                      passwd="GukgV4Au9d2pN4H6t",
#                      database="mydatabase")

db = pymysql.connect(host="212.1.211.51",
                     user="u948493795_rootx",
                     passwd="Soulcodeacademy1#",
                     database="u948493795_library")


# variável de instanciamento do nosso banco de dados
cursor = db.cursor()
cursor.execute('SELECT * FROM `tblbooks`')

numrows = int(cursor.rowcount)
linhas = cursor.fetchall()

print('Número total de registros encontrados: %d' % numrows)
print('\nMostrando resultados...')

for linha in linhas:
    print(f'{linha[0]} -> {linha[1]}')