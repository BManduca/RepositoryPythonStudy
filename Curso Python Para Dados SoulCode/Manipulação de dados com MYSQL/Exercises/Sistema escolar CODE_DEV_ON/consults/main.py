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

# variável de instanciamento do nosso banco de dados
cursor = db.cursor()

"""

Faça as seguintes consultas:

- Liste todos os registros de sua tabela. OK

- Liste apenas nome e matrícula dos alunos do BCW23. OK

- Liste apenas o nome dos alunos que tiverem o sobrenome Lima. OK

- O aluno Carlos Augusto está na turma errada. Matricule o mesmo no BCW25. OK

- O aluno José Vinicius desistiu do curso, ele deve ser excluído do sistema. OK

"""


def execute_data():
    sql = "SELECT * FROM alunos"
    # sql = "SELECT nome, matricula FROM alunos WHERE turma LIKE '%BCW23%'"
    # sql = "SELECT nome FROM alunos where nome LIKE '%Lima%'"
    # sql = "UPDATE alunos SET turma = 'BCW25' WHERE matricula = 'MAT90552'"
    # sql = "DELETE FROM alunos WHERE matricula = 'MAT90557'"

    cursor.execute(sql)

    # db.commit()

    res = cursor.fetchall()
    
    imprimirLinha(2)
    for x in res:
        print(x)
    imprimirLinha(2)

    # imprimirLinha(1)
    # imprimirMensagem(f'{cursor.rowcount} linha(s) atualizada(s)!', 2)
    # imprimirMensagem(f'{cursor.rowcount} linha(s) deletada(s)!', 1)
    # imprimirLinha(1)


execute_data()
