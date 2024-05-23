"""
    - Alimente a tabela com dados
"""

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
    print('-=-' * 20)
    print(colors[0], end='')


db = pymysql.connect(host='localhost',
                     user='Manduca',
                     password='h3H@rSAuDK)@!Eu_',
                     database='code_dev_on_new_system_db')


def insert_data_table():
    cursor = db.cursor()

    sql = "INSERT INTO alunos (nome, matricula, turma) VALUES (%s, %s, %s)"

    # val = ("José Vinícius", "MAT90556", "BCW25")

    val = [
        ("José Lima", "MAT90551", "BCW22"),
        ("Carlos Augusto", "MAT90552", "BCW22"),
        ("Lívia Lima", "MAT90553", "BCW22"),
        ("Sandra Gomes", "MAT90554", "BCW23"),
        ("João Augusto", "MAT90555", "BCW23"),
        ("Breno Lima", "MAT90556", "BCW24"),
        ("José Vinícius", "MAT90557", "BCW25")
    ]

    # executando comando de insert com o data presente em val
    # cursor.execute(sql, val)
    cursor.executemany(sql, val)

    # necessário para que o database seja modificado
    db.commit()

    imprimirLinha(4)
    imprimirMensagem(f'{cursor.rowcount} linha(s) adicionada(s)', 2)
    imprimirLinha(4)


insert_data_table()
