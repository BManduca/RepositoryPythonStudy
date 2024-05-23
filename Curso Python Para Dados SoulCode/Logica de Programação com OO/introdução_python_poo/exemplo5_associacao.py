"""
    NESTE EXMPLO DA AULA DE ASSOCIAÇÃO ESTAREMOS FAZENDO A CRIAÇÃO DE DUAS CLASSES (ESCRITOR E CANETA),
    ONDE A CANETA SERÁ A CLASSE QUE SERÁ PARTE COMO ATRÍBUTO DA CLASSE ESCRITOR, DESTA FORMA,
    ESTAREMOS PRESENCIANDO UMA ASSOCIAÇÃO.
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


class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        # atríbuto definido como privado para essa opc não possa ser alterada por fora
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        imprimirLinha(1)
        imprimirMensagem(f'A caneta {self.__marca.upper()} está escrevendo...', 2)
        imprimirLinha(1)


escritor1 = Escritor('Brunno')
caneta1 = Caneta('Crown')

escritor1.ferramenta = caneta1
escritor1.ferramenta.escrever()
