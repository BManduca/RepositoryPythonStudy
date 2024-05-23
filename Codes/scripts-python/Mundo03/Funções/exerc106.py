"""
    FAÇA UM MINI-SISTEMA QUE UTILIZA O INTERACTIVE HELP DO PYTHON.
    O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER.

    QUANDO O USUÁRIO DIGITAR A PALAVRA 'FIM', O PROGRAMA SE ENCERRARÁ.

    OBS.: USE CORES.
"""

from os import system
from time import sleep


colors = ('\033[m',         # 0 - sem cores
          '\033[0;30;41m',  # 1 - vermelho
          '\033[0;30;42m',  # 2 - verde
          '\033[0;30;43m',  # 3 - amarelo
          '\033[0;30;44m',  # 4 - azul
          '\033[0;30;45m',  # 5 - roxo
          '\033[7;37;40m'   # 6 - branco
          )


def imprimirTitulo(mens, cor=0):
    tam = len(mens)
    print()
    print(colors[cor], end='')
    print('~' * tam)
    print(f'{mens}')
    print('~' * tam)
    print(colors[0], end='')
    print()
    sleep(1)


def ajuda(com):
    imprimirTitulo(f'   ACESSANDO O MANUAL DO COMANDO \'{com.upper()}\'   ', 4)
    print(colors[6], end='')
    help(com)
    print(colors[0], end='')
    sleep(2)


# programa principal
comando = ''

while True:
    imprimirTitulo('   SISTEMA DE AJUDA PyHELP   ', 2)
    comando = str(input('FUNÇÃO OU BIBLIOTECA ==> '))

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

imprimirTitulo('  ATÉ LOGO!!  ', 1)
