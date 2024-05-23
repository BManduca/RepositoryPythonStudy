"""

ESTE MÓDULO FORNECE FUNÇÕES DE OPERAÇÕES MATEMÁTICAS BÁSICAS, COMO
POR EXEMPLO: SOMAR, SUBTRAIR, DIVIDIR E MULTIPLICAR. ELE AINDA TAMBÉM
POSSUI UMA FUNÇÃO PARA IMPRIMIR AS MENSAGENS.

"""


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


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def dividir(a, b):
    return a/b


def multiplicar(a, b):
    return a * b


# imprimirLinha(1)
# imprimirMensagem(f'Soma: {somar(4, 9)}', 2)
# imprimirMensagem(f'Subtração: {subtrair(7, 5)}', 2)
# imprimirMensagem(f'Divisão: {dividir(10, 3):.2f}', 2)
# imprimirMensagem(f'Multiplicação: {multiplicar(4, 9.5)}', 2)
# imprimirLinha(1)

