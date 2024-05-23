"""
    para criar uma classe abstrata,
    é preciso utilizar o método ABC (abstract method)

"""

from abc import ABC, abstractmethod

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


class letras:
    # para trabalhar e tratar essa classe, como uma classe abstrata
    # é preciso utilizar @abstractmethod
    @abstractmethod
    def mostrarTipo(self):
        imprimirMensagem('Eu sou uma classe abstrata!', 4)


class A(letras):
    def __init__(self, description):
        self.description = description

    def imprimir(self):
        imprimirMensagem('Aqui é um método diferente!', 2)


letraa = A("Letra A")
imprimirLinha(1)
letraa.mostrarTipo()
letraa.imprimir()
imprimirLinha(1)
